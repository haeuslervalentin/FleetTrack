# Umsetzungskonzept

## 1. Ziel des MVP

Der erste MVP soll ausschließlich diesen Ablauf beweisen:

```text
Benutzerfrage in VS Code/Copilot
→ MCP-Tool list_vehicles
→ Python-Service
→ SQLite-Datenbank
→ Fahrzeugliste als Antwort
```

Beispiel:

```text
Liste mir alle Fahrzeuge auf.
```

Erwartete Antwort:

```text
In der Flotte befinden sich 3 Fahrzeuge:

1. BMW X3 – W-123AB – 58.200 km – verfügbar
2. Mercedes-Benz Sprinter – W-456CD – 124.500 km – Wartung
3. Volkswagen Caddy – W-789EF – 31.700 km – verfügbar
```

---

## 2. Benennungskonzept

### Dateien

Dateinamen werden kleingeschrieben und mit Unterstrichen geschrieben:

```text
vehicle_service.py
test_vehicle_service.py
seed_db.py
```

### Funktionen

Funktionen verwenden Verben:

```text
list_vehicles()
get_vehicle()
create_vehicle()
update_vehicle()
delete_vehicle()
```

Nicht verwenden:

```text
vehicle_data()
do_vehicle()
thing()
```

### MCP-Tools

MCP-Tools sollen eindeutig und verständlich heißen:

```text
list_vehicles
get_vehicle
create_vehicle
add_mileage
schedule_service
```

### Datenbankmodelle

Modelle werden im Singular und mit Großbuchstaben benannt:

```text
Vehicle
Driver
Assignment
Service
```

### Statuswerte

Statuswerte werden immer gleich geschrieben:

```text
available
maintenance
inactive
```

Keine Mischformen wie:

```text
Available
wartung
in_service
```

---

## 3. Geplante Projektstruktur

```text
FleetTrack/
├── backend/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── seed_db.py
│   └── services/
│       ├── vehicle_service.py
│       ├── driver_service.py
│       └── service_service.py
├── mcp_server/
│   ├── server.py
│   ├── tools/
│   │   ├── vehicles.py
│   │   ├── drivers.py
│   │   └── services.py
│   └── resources/
├── data/
│   ├── seed.json
│   └── fleet.db
├── tests/
│   ├── unit/
│   ├── integration/
│   └── user_tests/
├── tools/
│   └── data-validator-csharp/
├── Dockerfile
├── docker-compose.yml
└── pyproject.toml
```

---

## 4. Normale technische Tests

### Unit-Tests

Unit-Tests testen einzelne Funktionen isoliert.

Beispiele:

```text
list_vehicles() gibt eine Liste zurück
```

```text
Jedes Fahrzeug besitzt die erwarteten Felder
```

```text
Fahrzeug-IDs sind eindeutig
```

```text
Ungültige Statuswerte werden abgelehnt
```

```text
Ein negatives Mileage wird abgelehnt
```

Unit-Tests werden häufig ausgeführt:

```bash
uv run pytest tests/unit
```

### Integrationstests

Integrationstests prüfen mehrere Komponenten gemeinsam:

```text
seed.json
→ Datenbank
→ Service
→ Ergebnis
```

Beispiele:

```text
Die Seed-Datei wird korrekt importiert
```

```text
list_vehicles() liest tatsächlich aus SQLite
```

```text
Ein Fahrzeug mit maintenance wird korrekt zurückgegeben
```

```text
Der MCP-Server stellt list_vehicles bereit
```

Ausführung:

```bash
uv run pytest tests/integration
```

### MCP-Tests

Diese Tests prüfen speziell die MCP-Schnittstelle:

```text
Ist list_vehicles registriert?
```

```text
Hat das Tool die richtige Beschreibung?
```

```text
Liefert das Tool gültiges JSON?
```

```text
Kann ein MCP-Client das Tool aufrufen?
```

### Docker-Tests

Docker muss getestet werden, weil der Server dort später präsentiert wird:

```text
docker compose build funktioniert
```

```text
docker compose up startet den Server
```

```text
Port 8000 ist erreichbar
```

```text
MCP-Client kann über /mcp zugreifen
```

---

## 5. User-Tests

User-Tests testen nicht den Code, sondern ob ein normaler Benutzer das System versteht und erfolgreich verwendet.

### User-Test 1: Fahrzeuge anzeigen

Aufgabe für die Testperson:

```text
Finde heraus, welche Fahrzeuge in der Flotte gespeichert sind.
```

Erwartung:

- Die Person schreibt eine natürliche Frage.
- Copilot ruft `list_vehicles` auf.
- Die Fahrzeugliste wird verständlich angezeigt.

### User-Test 2: Fahrzeugstatus verstehen

Aufgabe:

```text
Welche Fahrzeuge befinden sich gerade in Wartung?
```

Erwartung:

```text
Mercedes-Benz Sprinter – W-456CD
```

### User-Test 3: Ungültige Anfrage

Aufgabe:

```text
Zeige mir das Fahrzeug mit der ID 999.
```

Erwartung:

```text
Es wurde kein Fahrzeug mit der ID 999 gefunden.
```

### User-Test 4: Ungenaue Sprache

Aufgabe:

```text
Welche Autos haben wir?
```

Erwartung:

- Das System erkennt, dass Fahrzeuge gemeint sind.
- Das Tool `list_vehicles` wird verwendet.

### User-Test-Dokumentation

Jeder User-Test sollte dokumentiert werden:

```text
Test-ID: UT-001
Aufgabe: Alle Fahrzeuge anzeigen
Testperson: Kollege 1
Ergebnis: Erfolgreich
Probleme: Keine
Verbesserung: Keine
```

---

## 6. Tool-Beschreibungen

Jedes MCP-Tool braucht eine klare Beschreibung.

Beispiel:

```text
list_vehicles:
Liefert alle Fahrzeuge aus der FleetTrack-Datenbank.
Das Tool verändert keine Daten.
```

Bei Schreibfunktionen muss klar sein:

```text
create_vehicle:
Legt ein neues Fahrzeug in der Flotten-Datenbank an.
Das Tool verändert dauerhaft Daten.
Das Kennzeichen muss eindeutig sein.
```

Das hilft Copilot zu entscheiden, wann ein Tool verwendet werden soll.

---

## 7. Entwicklungsreihenfolge

### Phase 1: Grundlage

- Python-Projekt
- `uv`
- SQLite
- SQLAlchemy
- Fahrzeugmodell
- Seed-Daten

### Phase 2: Lesen

- `list_vehicles()` Service
- Unit-Tests
- MCP-Tool `list_vehicles`
- MCP Inspector
- Docker

### Phase 3: Erstes Schreiben

- Pydantic-Schemas
- `create_vehicle()`
- Prüfung auf doppelte Kennzeichen
- Bestätigung im User-Test
- Integrationstest

### Phase 4: Weitere Funktionen

- Fahrer
- Fahrzeugzuweisungen
- Kilometerstände
- Wartungen
- Statistiken

### Phase 5: Präsentation

- Architekturdiagramm
- Testprotokoll
- Demonstrationsablauf
- Erklärung von MCP, Tools und SQLite
- Vergleich mit klassischer REST-API

---

## 8. Definition of Done

Eine Funktion gilt erst als fertig, wenn:

- der Code funktioniert,
- die Funktion sinnvoll benannt ist,
- mindestens ein Unit-Test existiert,
- ein Integrationstest vorhanden ist, falls Datenbankzugriff beteiligt ist,
- das MCP-Tool getestet wurde,
- Fehlerfälle behandelt werden,
- die Funktion in Docker funktioniert,
- ein User-Test durchgeführt wurde,
- die Dokumentation aktualisiert wurde.

