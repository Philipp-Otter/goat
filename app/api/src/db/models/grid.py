from typing import TYPE_CHECKING, List, Optional

from geoalchemy2 import Geometry
from sqlalchemy import SmallInteger
from sqlmodel import (
    BigInteger,
    Column,
    Field,
    Float,
    ForeignKey,
    Index,
    Integer,
    Relationship,
    SQLModel,
)

if TYPE_CHECKING:
    from .heatmap import ReachedEdgeHeatmapGridCalculation
    from .study_area import StudyArea
    from .traveltime_matrix import TravelTimeMatrixWalking

from ._link_model import StudyAreaGridVisualization


class GridVisualization(SQLModel, table=True):
    __tablename__ = "grid_visualization"
    __table_args__ = {"schema": "basic"}

    id: Optional[int] = Field(
        sa_column=Column(BigInteger(), primary_key=True, autoincrement=False),
    )
    area_isochrone: float = Field(sa_column=Column(Float(53)))
    percentile_area_isochrone: int = Field(sa_column=Column(SmallInteger, nullable=True))
    population: Optional[int]
    percentile_population: int = Field(sa_column=Column(SmallInteger, nullable=True))
    geom: str = Field(
        sa_column=Column(
            Geometry(geometry_type="Polygon", srid="4326", spatial_index=False),
            nullable=False,
        )
    )

    study_areas: List["StudyArea"] = Relationship(
        back_populates="grid_visualizations", link_model=StudyAreaGridVisualization
    )
    grid_calculations: List["GridCalculation"] = Relationship(back_populates="grid_visualization")

Index("idx_grid_visualization_geom", GridVisualization.__table__.c.geom, postgresql_using="gist")

class GridCalculation(SQLModel, table=True):
    __tablename__ = "grid_calculation"
    __table_args__ = {"schema": "basic"}

    id: Optional[int] = Field(
        # TODO: Add next value to the sequence
        sa_column=Column(BigInteger(), primary_key=True, autoincrement=False)
    )
    geom: str = Field(
        sa_column=Column(
            Geometry(geometry_type="Polygon", srid="4326", spatial_index=False),
            nullable=False,
        )
    )
    grid_visualization_id: int = Field(
        sa_column=Column(
            BigInteger,
            ForeignKey("basic.grid_visualization.id", ondelete="CASCADE"),
            nullable=False,
        )
    )
    grid_visualization: "GridVisualization" = Relationship(back_populates="grid_calculations")
    traveltime_matrix_walking: "TravelTimeMatrixWalking" = Relationship(back_populates="grid_calculation")


Index("idx_grid_caclulation_geom", GridCalculation.__table__.c.geom, postgresql_using="gist")

