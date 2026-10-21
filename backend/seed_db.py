import json # for json file handling
from pathlib import Path

from backend.database import SessionLocal # earlier created session
from backend.models import Vehicle # self created datamodel

BASE_DIR = Path(__file__).resolve().parent.parent
SEED_PATH = BASE_DIR / "data" / "seed.json"


def read_json(file_path: Path) -> list[dict]:
    """
    Reads a json with the given file_path.
    Savely tries to load the json file and expects FileNotFoundErrors and json.JSONDecodeError
    Returns a list of dicts with vehicle datas.
    """
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Seed-Datei not found: {file_path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"JSON unworthy in {file_path}: {error}") from error

    if not isinstance(data, list):
        raise ValueError("The seed-file must contain a list of vehicles.")

    return data


def seed_database() -> None:
    """fills the db with the data from the seed.json."""
    vehicle_data = read_json(SEED_PATH)

    with SessionLocal() as session: # opening the session
        existing_vehicle = session.query(Vehicle).first()

        if existing_vehicle is not None: # if sth is already saved do not override i
            print("The database has already vehicles")
            return

        vehicles = [
            Vehicle(
                id=vehicle["id"],
                manufacturer=vehicle["manufacturer"],
                model=vehicle["model"],
                license_plate=vehicle["license_plate"],
                year=vehicle["year"],
                mileage=vehicle["mileage"],
                status=vehicle["status"],
            )
            for vehicle in vehicle_data
        ]

    session.add_all(vehicles) # save the vehicles in the db 
    session.commit() # close it 

    print(f"{len(vehicles)} vehicles were imported.")


if __name__ == "__main__":
    seed_database()
