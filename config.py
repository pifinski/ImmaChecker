# Das exportierte Airtable CSV
csv = "Versuch ImmaChecker - Tabellenblatt1.csv"

# Der Ordner, in dem die Immatrikulationsbescheinigungen gespeichert werden sollen
imma_path = "Immatrikulationsbescheinigungen"

# Der Ordner, in dem die Ergebnisse gespeichert werden sollen
output_pfad = "output"

#Anbieter: "AirTable oder "Google" bitte entfernt hier das # vor dem jeweilig gewählten Anbieter hier ist aittable ausgewählt
anbieter = "AirTable"
#anbieter = "Google"

# Die Studiengänge, die mit auf die Medis dürfen, genau so wie sie in der Immatrikulationsbescheinigung stehen
studiengaenge = ["Zahnmedizin", "Humanmedizin", "Medizin", "Molekularmedizin"]

# Die erlaubten Endungen der Emailadresse
erlaubte_email_domains = []

# Das aktuelle Semester wie in der Immatrikulationsbescheinigung.
# Falls es hier mehrere Möglichkeiten gibt, könnt ihr wie bei den Studiengängen
# eine Liste erstellen (also z. B. ["semester1", "semester2"]).
semester = ["Wintersemester 2022/2023", "Sommersemester 2022"]

# Die Spaltennamen, die ihr für das Airtable verwendet habt
vorname_spalte = "Vorname"
nachname_spalte = "Nachname"
email_spalte = "Nutzername"
imma_bescheinigung_spalte = "Studeinbescheinigung: name.vorname.pdf"

# Das Geburtsdatum
# Falls diese Spalte leer ist (geburtsdatum_spalte = ""), wird nicht überprüft, ob jemand volljährig ist
geburtsdatum_spalte = ""
# Das Geburtsdatumsformat, wie es in den Immatrikulationsbescheinigungen steht.
# Falls euer Geburtsdatum anders aussieht als tt.mm.JJJJ könnt ihr es hier anpassen
geburtsdatum_format = "%d.%m.%Y"

# Der erste Tag der Medis (also der Tag, an dem die Leute Geburtstag haben müssen, um 18 zu sein)
medis_erster_tag = "08.06.2023"

# Die Regular Expression, die den Namen herausfiltert.
# Wendet euch bei Fragen an mich oder an den Informatiker eures Vertrauens
namen_regex = r"(?:Herr|Frau)\s+([A-zÀ-ú@0-9- üÜ]*)\s+(?:ist\s+im)"

# Ab hier kommen Sachen die nur verändert werden sollten,
# wenn ihr wisst was ihr macht (oder neugierig seid)
# Das Regex für den Airtable Imma Upload

uploaded_imma_regex_airtable =  "(.*) \((http[s].*)\)"
uploaded_imma_regex_google = "(?:.*id=)(\w*)"


# Das Format des Geburtsdatums in Airtable
airtable_geburtstagsdatum_format = "%Y-%m-%d"

# Der maximale Levensthein Wert zum Namensvergleich
levensthein_cutoff = 66
