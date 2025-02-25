CREATE OR REPLACE FUNCTION basic.heatmap_population(active_study_area_id integer, modus_input text DEFAULT 'default', scenario_id_input integer DEFAULT 0)
RETURNS TABLE(grid_visualization_id bigint, population float, percentile_population integer, modus text, geom geometry)
LANGUAGE plpgsql
AS $function$
BEGIN 
	
	IF modus_input IN ('default', 'comparison') THEN 
		DROP TABLE IF EXISTS population_default;
		CREATE TEMP TABLE population_default AS 
		SELECT * FROM basic.prepare_heatmap_population(active_study_area_id, 'default', scenario_id_input);
	END IF; 
	IF modus_input IN ('scenario','comparison') THEN 
		DROP TABLE IF EXISTS population_scenario;
		CREATE TEMP TABLE population_scenario AS 
		SELECT * FROM basic.prepare_heatmap_population(active_study_area_id, 'scenario', scenario_id_input);
	END IF;
	IF modus_input IN ('comparison') THEN 
		ALTER TABLE population_default ADD PRIMARY KEY(grid_visualization_id); 
		ALTER TABLE population_scenario ADD PRIMARY KEY(grid_visualization_id); 
		DROP TABLE IF EXISTS population_comparison;
		
		CREATE TEMP TABLE population_comparison AS 
		WITH pop_difference AS 
		(
			SELECT d.grid_visualization_id, (COALESCE(s.population,0) - COALESCE(d.population,0)) AS population, d.geom
			FROM population_default d, population_scenario s
			WHERE d.grid_visualization_id = s.grid_visualization_id
		) 
		SELECT p.grid_visualization_id, p.population, 
		CASE 
		WHEN p.population = 0 THEN 0
		WHEN p.population < -1000 THEN -5 
		WHEN p.population BETWEEN -1000 AND -500 THEN -4 
		WHEN p.population BETWEEN -500 AND -200 THEN -3 
		WHEN p.population BETWEEN -200 AND -80 THEN -2 
		WHEN p.population BETWEEN -80 AND -1 THEN -1 
		WHEN p.population BETWEEN 1 AND 80 THEN 1 
		WHEN p.population BETWEEN 80 AND 200 THEN 2
		WHEN p.population BETWEEN 200 AND 500 THEN 3 
		WHEN p.population BETWEEN 500 AND 1000 THEN 4 
		WHEN p.population  > 1000 THEN 5 END AS percentile_population, p.geom 
		FROM pop_difference p;

	END IF; 
		
	IF modus_input = 'default' THEN 
		RETURN query 
		SELECT p.grid_visualization_id, p.population, COALESCE(p.percentile_population, 0), modus_input AS modus, p.geom 
		FROM population_default p;
	ELSEIF modus_input = 'scenario' THEN 
		RETURN query 
		SELECT p.grid_visualization_id, p.population, COALESCE(p.percentile_population, 0), modus_input AS modus, p.geom 
		FROM population_scenario p;
	ELSEIF modus_input = 'comparison' THEN 
		RETURN query 
		SELECT p.grid_visualization_id, p.population, COALESCE(p.percentile_population, 0), modus_input AS modus, p.geom 
		FROM population_comparison p;
	END IF; 

END
$function$;

/*
DROP TABLE IF EXISTS default_pop;
CREATE TABLE default_pop AS 
SELECT * 
FROM basic.heatmap_population(1,'default',0)

DROP TABLE IF EXISTS scenario_pop;
CREATE TABLE scenario_pop AS 
SELECT * 
FROM basic.heatmap_population(1,'scenario',13)

DROP TABLE IF EXISTS comparison_pop;
CREATE TABLE comparison_pop AS 
SELECT * 
FROM basic.heatmap_population(1,'comparison',13)
*/
