from backend.database import Base, engine
from backend.models import Vehicle


def init_db() -> None:
    """Initialies the database with the earlier build engine"""

    Base.metadata.create_all(bind=engine)
    print("Datenbanktabellen wurden erstellt.")


if __name__ == "__main__":
    init_db()
