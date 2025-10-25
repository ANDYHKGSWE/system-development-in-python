# Systemövervakare i Python

Detta är ett enkelt kommandoradsverktyg för att övervaka systemresurser som CPU, minne och diskanvändning.

## Funktioner

- **Övervaka systemet**: Se aktuell användning av CPU, minne och disk.
- **Skapa larm**: Sätt anpassade larmgränser för CPU, minne och disk. När en resurs överskrider gränsen visas en varning.
- **Realtidsläge**: Kör övervakaren i ett aktivt läge som kontinuerligt uppdaterar och varnar vid larm.

## Installation

1.  **Klona repot**:

    ```bash
    git clone <repo-url>
    cd system-development-in-python/python-monitor
    ```

2.  **Skapa en virtuell miljö**:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Installera beroenden**:
    ```bash
    pip install -r requirements.txt
    ```

## Användning

För att starta programmet, kör följande kommando från `python-monitor`-mappen:

```bash
python3 src/app.py
```

Du kommer att mötas av en huvudmeny där du kan välja olika alternativ för att övervaka systemet och hantera larm.
