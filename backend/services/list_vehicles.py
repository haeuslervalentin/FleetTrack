from sqlalchemy import select

from backend.database import SessionLocal  # earlier created session
from backend.models import Vehicle


def list_vehicles() -> list[dict]:
    """
    Lists a num of vehicles from the db.
    Returns a list of dicts with vehicle data.
    """

    with SessionLocal() as session:
        stmt = select(Vehicle)
        vehicles_objects = session.execute(stmt).scalars().all()

        return [
            {
                "id": v.id,
                "manufacturer": v.manufacturer,
                "model": v.model,
                "license_plate": v.license_plate,
                "year": v.year,
                "mileage": v.mileage,
                "status": v.status,
            }
            for v in vehicles_objects
        ]
