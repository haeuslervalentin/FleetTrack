from backend.database import SessionLocal # earlier created session

def list_vehicle() -> list[dict]:
    """
    Lists a num of vehicles from the db.
    Returns a list of dicts with vehicle data.
    """

    with SessionLocal() as session:
        vehicles = session.query(vehicles)

        print(f"{len()}")
        return vehicles 

