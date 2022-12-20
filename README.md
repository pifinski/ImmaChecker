# ImmaChecker2.0

How to make Immatrikulationschecking easy!

## Wie führe ich das Ganze aus?

### AirTable
1. Erstellt euch einen kostenlosen AirTable-Account auf www.airtable.com
1. Erstellt euer Formular und baut ein Upload-Feld ein! (P.S. betont mehrfach, dass es nur originale PDF-Dateien sein sollen, das spart euch unfassbar viel Arbeit im Nachhinein!)
1. Verteilt den Link und lasst eure Studis sich eintragen.
1. Nach Ablauf der Fristen ladet euch das AirTable als Tabelle (.csv) runter ([Anleitung](https://support.airtable.com/docs/download-a-view-to-csv)).
1. Stellt sicher, dass ihr Python3 auf eurem PC installiert habt. Dazu könnt ihr in der Befehlseingabe `python --version`, `py --version`, `python.exe --version` oder `py.exe --version` eingeben. Wenn keins davon funktioniert habt ihr Python nicht installiert.
    - Es sollte so etwas wie `Python 3.10.8` zurückgegeben werden. Das wichtige ist die erste Zahl, die eine `3` sein sollte.
    - Falls ihr Python nicht installiert habt könnt ihr es euch über folgenden Link runterladen: https://www.python.org/downloads/release/python-3913/
1. Ladet euch die Dateien herunter (`requirements.txt`, `config.py` und `imma_checker.py`). Das geht bei Github über den grünen Knopf rechts oben: `Code` -> `Download Zip`. Entpackt die Zip-Datei. Anschließend solltet ihr einen Ordner mit den Dateien haben.
1. Kopiert die Airtable CSV Datei in den gleichen Ordner.
1. Passt `config.py` an. Wenn es einen Fehler gibt liegt es wahrscheinlich hier dran. Achtet insbesondere auf `name_regex`. Bei Fragen könnt ihr gerne schreiben.
1. Öffnet eure Befehlseingabe, falls ihr das noch nicht gemacht habt. Ab jetzt arbeiten wir dort weiter.
    - Navigiert in den heruntergeladenen Ordner ([Kurzanleitung](https://praxistipps.chip.de/windows-in-der-konsole-navigieren-so-gehts_38848)) und gebt die folgenden Befehle ein.
    - Eventuell müsst ihr `python` durch `py` oder `python.exe` bzw. `py.exe`.
    - Windows:
        - `python -m pip install virtualenv`
        - `python -m virtualenv venv` (Das kann ein bisschen dauern)
        - `venv\Scripts\activate` (Wenn bisher alles geklappt hat solltet ihr `(venv)` vor jeder neuen Eingabezeile sehen)
        - `pip install -r requirements.txt`
        - `python imma_checker.py`
    - Apple
        - `python -m pip install virtualenv`
        - `python -m virtualenv venv`  (Das kann ein bisschen dauern)
        - `source venv/bin/activate` (Wenn bisher alles geklappt hat solltet ihr `(venv)` vor jeder neuen Eingabezeile sehen)
        - `pip install -r requirements.txt`
        - `python imma_checker.py`
1. Das Programm läuft jetzt (und sollte nicht zu lange brauchen). Fehler werden in den Outputs gespeichert bzw. direkt auf der Kommandozeile angezeigt.
1. Nachdem das Programm beendet wurde findet ihr im Output-Ordner drei Tabellen. In der Fehlertabelle sind jeweils die Gründe angegeben, die ihr noch einmal händisch überprüfen solltet. Zur Überprüfung der Namen wurden zwei Spalten hinzugefügt: `Levenshteindistanz` und `bester Namenskandidat`. Das Script sucht in der Immatrikulationsbescheinigung nach Namen. Wenn ein Name gefunden wurde, wird er mit der Angabe in der Tabelle verglichen. Der Wert, der bei diesem Vergleich herauskommt ist die Levenshteindistanz.  Je näher sie an 100 ist, desto sicherer ist, das der Name stimmt. Ist die Distanz niedrig solltet ihr das PDF nochmal überprüfen.

Bei Fragen meldet euch gerne!

### Google-Forms
1. Ihr erstellt euer Google-Form entsprechend eurer Vorstellungen (CAVE! File-Upload Felder funktionieren bei "normalen" Google-Accounts nur für Personen mit Google Konto, Für Google-Business-Konten geht es auch ohne Anmeldung der Teilnehmer) 
1. Nach Ablauf der Fristen ladet euch das GoogleForm als Tabelle (.csv) runter ([Anleitung](https://www.spreadsheetclass.com/google-sheets-export-csv/)).
1. Stellt sicher, dass ihr Python3 auf eurem PC installiert habt. Dazu könnt ihr in der Befehlseingabe `python --version`, `py --version`, `python.exe --version` oder `py.exe --version` eingeben. Wenn keins davon funktioniert habt ihr Python nicht installiert.
    - Es sollte so etwas wie `Python 3.10.8` zurückgegeben werden. Das wichtige ist die erste Zahl, die eine `3` sein sollte.
    - Falls ihr Python nicht installiert habt könnt ihr es euch über folgenden Link runterladen: https://www.python.org/downloads/release/python-3913/
1. Ladet euch die Dateien herunter (`requirements.txt`, `config.py` und `imma_checker.py`). Das geht bei Github über den grünen Knopf rechts oben: `Code` -> `Download Zip`. Entpackt die Zip-Datei. Anschließend solltet ihr einen Ordner mit den Dateien haben.
1. Um über das Skript an die hochgeladenen Dateien zu kommen benötigt ihr eine eigene API mit Zugangsdaten, diese erstellt ihr wie hier beschrieben: https://docs.iterative.ai/PyDrive2/quickstart/#authentication
    - die heruntergeladene JSON-Datei speichert ihr als `client_secrets.json`im selben Ordner ab
1. Kopiert die Google-Forms CSV Datei in den gleichen Ordner.
1. Passt `config.py` an. Wenn es einen Fehler gibt liegt es wahrscheinlich hier dran. Achtet insbesondere auf `name_regex`. Bei Fragen könnt ihr gerne schreiben.
1. Öffnet eure Befehlseingabe, falls ihr das noch nicht gemacht habt. Ab jetzt arbeiten wir dort weiter.
    - Navigiert in den heruntergeladenen Ordner ([Kurzanleitung](https://praxistipps.chip.de/windows-in-der-konsole-navigieren-so-gehts_38848)) und gebt die folgenden Befehle ein.
    - Eventuell müsst ihr `python` durch `py` oder `python.exe` bzw. `py.exe`.
    - Windows:
        - `python -m pip install virtualenv`
        - `python -m virtualenv venv` (Das kann ein bisschen dauern)
        - `venv\Scripts\activate` (Wenn bisher alles geklappt hat solltet ihr `(venv)` vor jeder neuen Eingabezeile sehen)
        - `pip install -r requirements.txt`
        - `python imma_checker.py`
    - Apple
        - `python -m pip install virtualenv`
        - `python -m virtualenv venv`  (Das kann ein bisschen dauern)
        - `source venv/bin/activate` (Wenn bisher alles geklappt hat solltet ihr `(venv)` vor jeder neuen Eingabezeile sehen)
        - `pip install -r requirements.txt`
        - `python imma_checker.py`
1. Das Programm läuft jetzt (und sollte nicht zu lange brauchen). Fehler werden in den Outputs gespeichert bzw. direkt auf der Kommandozeile angezeigt.
1. Nachdem das Programm beendet wurde findet ihr im Output-Ordner drei Tabellen. In der Fehlertabelle sind jeweils die Gründe angegeben, die ihr noch einmal händisch überprüfen solltet. Zur Überprüfung der Namen wurden zwei Spalten hinzugefügt: `Levenshteindistanz` und `bester Namenskandidat`. Das Script sucht in der Immatrikulationsbescheinigung nach Namen. Wenn ein Name gefunden wurde, wird er mit der Angabe in der Tabelle verglichen. Der Wert, der bei diesem Vergleich herauskommt ist die Levenshteindistanz.  Je näher sie an 100 ist, desto sicherer ist, das der Name stimmt. Ist die Distanz niedrig solltet ihr das PDF nochmal überprüfen.

Bei Fragen meldet euch gerne!

## Fehlermeldungen und ihre Lösungen
```
[!] Beim Öffnen und Verarbeiten eines PDFs gab es einen Fehler:
        Name: Vorname Nachname
        Datei: immatrikulationsbescheinigungen/2.pdf
        cannot open broken document
```
Hier müsst ihr das Airtable erneut herunterladen, da der Link, über den die Immatrikulationsbescheinigungen heruntergeladen werden, abgelaufen ist.
