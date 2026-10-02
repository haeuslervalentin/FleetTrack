from backend.database import Base, engine
from backend.models import Vehicle


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
    print("Datenbanktabellen wurden erstellt.")


if __name__ == "__main__":
    init_db()
