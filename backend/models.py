from sqlalchemy import Integer, String # datatypes
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Vehicle(Base):
    """
    Datamodel Vehicle with fields:
    + id : int <<PK>>
    + manufacturer : STR(100)
    + model : STR(100)
    + license_plate : STR(20) unique 
    + year : int 
    + mileage : int
    + status : str(30)
    """
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    manufacturer: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    license_plate: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    mileage: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(30), nullable=False)
