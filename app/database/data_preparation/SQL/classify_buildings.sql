/*Performance issues with queries. Ideas for improvement:
- avoid update but rather write to new table
- experiment with HOT-Update
- Check if no residentials landuse from different table can be fused before intersection with buildings

*/

DO $$                  
    BEGIN 
        IF EXISTS
            ( SELECT 1
              FROM   information_schema.tables 
              WHERE  table_schema = 'public'
              AND    table_name = 'landuse'
            )
        THEN
			--Intersect with custom landuse table
        	ALTER TABLE landuse ADD COLUMN IF NOT EXISTS name text;
      
        	UPDATE buildings b 
        	SET residential_status = 'with_residents'
        	FROM landuse l
        	WHERE ST_Contains(l.geom,b.geom)
        	AND lower(name) ~~ ANY (SELECT UNNEST(select_from_variable_container('custom_landuse_with_residents_name')));
        
        	UPDATE buildings b 
        	SET residential_status = 'with_residents'
        	FROM landuse l
        	WHERE ST_Contains(l.geom,b.geom) = FALSE 
        	AND ST_Intersects(l.geom,b.geom)
			AND ST_Area(ST_Intersection(b.geom, l.geom)) / ST_Area(b.geom) > 0.5
        	AND lower(name) ~~ ANY (SELECT UNNEST(select_from_variable_container('custom_landuse_with_residents_name')));	
        
        	UPDATE buildings b
			SET residential_status = 'no_residents'
			FROM landuse l
			WHERE ST_Contains(l.geom,b.geom)
			AND b.residential_status = 'potential_residents'
			AND l.landuse IN(SELECT UNNEST(select_from_variable_container('custom_landuse_no_residents')));
		
			UPDATE buildings b
			SET residential_status = 'no_residents'
			FROM landuse l 
			WHERE ST_Contains(l.geom,b.geom) = FALSE 
			AND ST_Intersects(l.geom,b.geom)
			AND ST_Area(ST_Intersection(b.geom, l.geom)) / ST_Area(b.geom) > 0.5
			AND b.residential_status = 'potential_residents'
			AND l.landuse IN(SELECT UNNEST(select_from_variable_container('custom_landuse_no_residents')));
			
			/*
			WITH aois_buildings AS 
			(
				SELECT b.gid, b.geom 
				FROM buildings b, aois a
				WHERE ST_Intersects(b.geom, a.geom)
				AND b.residential_status = 'with_residents'
				AND a.amenity IN (SELECT UNNEST(select_from_variable_container('aois_no_residents')))
			),
			no_residents AS 
			(
				SELECT b.gid
				FROM aois_buildings b, landuse l 
				WHERE ST_Intersects(b.geom, l.geom) 
				AND l.landuse IN (SELECT UNNEST(select_from_variable_container('custom_landuse_no_residents'))) 
			)
			UPDATE buildings b SET residential_status = 'no_residents'
			FROM no_residents n
			WHERE b.gid = n.gid; 
			*/
        END IF ;
    END
$$ ;

DO $$                  
    BEGIN 
        IF EXISTS
            ( SELECT 1
              FROM   information_schema.tables 
              WHERE  table_schema = 'public'
              AND    table_name = 'landuse_additional'
            )
        THEN

			UPDATE buildings b 
			SET residential_status = 'no_residents'
			FROM landuse_additional l
			WHERE landuse IN (SELECT UNNEST(select_from_variable_container('custom_landuse_additional_no_residents')))
			AND ST_CONTAINS(l.geom,b.geom)
			AND b.residential_status = 'potential_residents';

        END IF ;
    END
$$ ;

CREATE TEMP TABLE osm_area_no_residents AS 
SELECT way AS geom 
FROM planet_osm_polygon 
WHERE landuse IN(SELECT UNNEST(select_from_variable_container('osm_landuse_no_residents')))
OR tourism IN(SELECT UNNEST(select_from_variable_container('tourism_no_residents')))
OR amenity IN(SELECT UNNEST(select_from_variable_container('amenity_no_residents')));

CREATE INDEX ON osm_area_no_residents USING GIST(geom);

UPDATE buildings b
SET residential_status = 'no_residents'
FROM osm_area_no_residents l
WHERE ST_Contains(l.geom,b.geom)
AND b.residential_status = 'potential_residents';

UPDATE buildings b
SET residential_status = 'no_residents'
FROM osm_area_no_residents l 
WHERE ST_Contains(l.geom,b.geom) = FALSE 
AND ST_Intersects(l.geom,b.geom)
AND ST_Area(ST_Intersection(b.geom, l.geom)) / ST_Area(b.geom) > 0.5
AND b.residential_status = 'potential_residents';

DROP TABLE IF EXISTS osm_area_no_residents ;

--Label all buildings that are not intersecting the custom land-use
DO $$                  
    BEGIN 
        IF EXISTS
            ( SELECT 1
              FROM   information_schema.tables 
              WHERE  table_schema = 'public'
              AND    table_name = 'landuse'
            )
        THEN					
        	UPDATE buildings
        	SET residential_status = 'no_residents'
        	FROM (
	        	SELECT b.gid
	        	FROM buildings b
	        	LEFT JOIN landuse l 
	        	ON st_intersects(b.geom,l.geom)
	        	WHERE l.gid IS NULL 
	        	AND b.residential_status = 'potential_residents'
        	) x
        	WHERE buildings.gid = x.gid;
 	
        END IF ;
    END
$$ ;

UPDATE buildings 
SET area = ST_AREA(geom::geography);

UPDATE buildings
SET residential_status = 'no_residents'
WHERE buildings.area < (SELECT select_from_variable_container_s('minimum_building_size_residential')::integer)
AND residential_status <> 'with_residents';

--Substract one level when POI on building (more classification has to be done in the future)

WITH x AS (
    SELECT DISTINCT b.gid
    FROM buildings b, pois p 
    WHERE st_intersects(b.geom,p.geom)
)
UPDATE buildings b
SET building_levels_residential = building_levels - 1
FROM x
WHERE b.gid = x.gid;

UPDATE buildings 
set building_levels_residential = building_levels
WHERE building_levels_residential IS NULL;

UPDATE buildings 
SET residential_status = 'with_residents'
WHERE residential_status = 'potential_residents';
 
UPDATE buildings 
SET gross_floor_area_residential = (building_levels_residential * area) + (roof_levels/2) * area 
WHERE residential_status = 'with_residents';

