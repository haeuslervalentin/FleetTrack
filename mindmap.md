```mermaid
mindmap
  root((Fuhrparkmanagement))
    Fuhrparkleitung
      Wie?
        PC
        E-Mail
      Was?
        Fahrzeuge verwalten
      Ausgangslage
        Viele Daten sind verteilt

    Fahrer
      Wie?
        App
        Telefon
      Was?
        Schäden und Tanken melden
      Ausgangslage
        Vieles wird noch manuell erfasst

    Werkstatt
      Wie?
        Telefon
        E-Mail
      Was?
        Wartungen und Reparaturen
      Ausgangslage
        Termine werden teilweise manuell geplant

    Buchhaltung
      Wie?
        PC
        E-Mail
      Was?
        Kosten und Rechnungen
      Ausgangslage
        Daten kommen aus verschiedenen Systemen

    Geschäftsführung
      Wie?
        Berichte
        E-Mail
      Was?
        Überblick über den Fuhrpark
      Ausgangslage
        Informationen müssen zusammengesucht werden
```

# Ausgangslage

# Verwaltungsaufwand im Fuhrpark

```text
                    ┌─────────────────────┐
                    │  Hoher Zeitaufwand  │
                    │  bei Verwaltung     │
                    └──────────┬──────────┘
                               │
     ┌─────────────────────────┼─────────────────────────┐
     │                         │                         │
     ▼                         ▼                         ▼

┌──────────────┐      ┌─────────────────┐      ┌─────────────────┐
│ Daten in     │      │ Manuelle        │      │ Termine werden  │
│ mehreren     │      │ Datenerfassung  │      │ übersehen       │
│ Systemen     │      │                 │      │                 │
└──────┬───────┘      └────────┬────────┘      └────────┬────────┘
       │                       │                        │
       ▼                       ▼                        ▼
 Informationen        Fehleranfälligkeit      Wartungen werden
 müssen gesucht       und Doppelarbeit        zu spät geplant

                              │
                              ▼

                  ┌─────────────────────────┐
                  │ Ausgangsproblem         │
                  │ Verwaltungsaufwand im   │
                  │ Fuhrpark ist zu hoch    │
                  └─────────────────────────┘

                              ▲
                              │

     ┌────────────────────────┼────────────────────────┐
     │                        │                        │
     ▼                        ▼                        ▼

┌──────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Fehlende     │     │ Schlechte       │     │ Hoher Aufwand   │
│ Übersicht    │     │ Kommunikation   │     │ bei Berichten   │
│ über Fuhrpark│     │ zwischen Rollen │     │ und Auswertungen│
└──────────────┘     └─────────────────┘     └─────────────────┘

```


```mermaid
mindmap
  root((Hoher Verwaltungsaufwand im Fuhrpark))

    Verteilte Daten
      Fahrzeugdaten in verschiedenen Systemen
      Informationen schwer auffindbar

    Manuelle Datenerfassung
      Viele Prozesse händisch
      Erhöhter Arbeitsaufwand

    Doppelarbeit
      Mehrfache Eingaben
      Zeitverlust

    Fehleranfälligkeit
      Übertragungsfehler
      Unvollständige Daten

    Fehlende Übersicht
      Kein zentraler Überblick
      Informationen müssen zusammengesucht werden

    Übersehene Wartungstermine
      Manuelle Terminverwaltung
      Risiko von Fristüberschreitungen

    Hoher Aufwand für Berichte
      Daten aus mehreren Quellen
      Berichte müssen manuell erstellt werden

    Lange Informationssuche
      Daten nicht zentral gespeichert
      Verzögerungen im Arbeitsablauf
```


# Projektvision
Unsere Projektvision ist es, ein digitales Fuhrparkmanagement-System zu entwickeln, das alle relevanten Informationen und Prozesse rund um Fahrzeuge, Fahrer, Wartungen und Kosten zentral in einer Plattform zusammenführt.
Wir möchten die derzeit verteilten Datenquellen und manuellen Arbeitsabläufe durch eine moderne, benutzerfreundliche Lösung ersetzen, die Transparenz schafft, Verwaltungsaufwände reduziert und Fehler minimiert.
Die Plattform soll allen Beteiligten, von Fahrern über die Fuhrparkleitung bis hin zur Buchhaltung und Geschäftsführung, den Zugriff auf aktuelle und relevante Informationen ermöglichen. Durch automatisierte Erinnerungen, digitale Meldungen und aussagekräftige Auswertungen werden Prozesse vereinfacht und Entscheidungen erleichtert.
Langfristig schaffen wir eine zentrale Informationsbasis, die den gesamten Fuhrpark effizienter, transparenter und zukunftssicher verwaltet.

---

# Projektumweltanalyse
```mermaid
graph TD
    %% Subgraph für interne Rollen
    subgraph Intern ["Interne Projektbeteiligte"]
        PL[Projektleiter<br/>Valentin]
        PM[Projektmanager<br/>Simon]
        AG[Projektauftraggeber<br/>Lehrer]
    end

    %% Subgraph für externe Rollen
    subgraph Extern ["Externe Einflüsse"]
        KONK[Konkurrenten<br/>Andere Gruppen]
    end

    %% Das zentrale Projekt
    P[Projekt: Digitales Fuhrparkmanagement]

    %% Verknüpfungen
    PL -->|+| P
    PM -->|+| P
    AG -->|+| P
    KONK -->|-| P

    %% Styling
    classDef intern fill:#d4edda,stroke:#155724,color:#000;
    classDef extern fill:#f8d7da,stroke:#721c24,color:#000;
    
    class AG,PL,PM intern;
    class KONK extern;
```

---

# Funktionsziele

## Funktionsziel 1: Zentrale Fuhrparkverwaltung

Bis zum Ende des Projekts ist eine zentrale Datenbank entwickelt, mit der Fahrzeugdaten (Marke, ...) in einer gemeinsamen Datenüberprüften (Zeitüberprüfung, Marke, PS, Wartung) Datenbank verwaltet werden.

**SMART-Bewertung:**
- **Spezifisch:** Zentrale Verwaltung aller geprüften Fuhrparkdaten
- **Messbar:** Alle Daten werden in einer Datenbank gespeichert und abrufbar gemacht
- **Attraktiv:** Reduzierung des Verwaltungsaufwands
- **Realistisch:** Mit Datenbank und API umsetzbar
- **Terminiert:** Bis zum Projektabschluss

---

## Funktionsziel 2: KI-gestützte Fuhrparkassistenz

Bis zum Ende des Projekts ist ein lokaler MCP-Server implementiert werden, der mindestens zwei Funktionen des Fuhrparkmanagements über natürliche Sprache ausführbar macht.

**SMART-Bewertung:**
- **Spezifisch:** Bereitstellung eines localen Server
- **Messbar:** Mindestens zwei über den MCP-Server nutzbare Funktionen
- **Attraktiv:** Schnellere Bedienung und Informationsbeschaffung
- **Realistisch:** Mit Python, MCP und einem LLM umsetzbar
- **Terminiert:** Bis zum Projektabschluss













# Umsetzungskonzept
sprache:python,c#
Variablenbennenung: snake_case
datenbank namen immer in einzahl
kennzeichnung des codes mit Namen -> mit comments
Entscheidungen wie Libs dokumentieren -> direkt im doc 
wie dokumentieren wir den code -> DocStrings
wie wird die gesamt Umsetzung dokumentiert -> docstring und readme
READNE schreiben
tests müssen dokumentiert sein -> eigenes md file wo tests kurz beschrieben werden

# DeadLine 12.Jänner