# Das exportierte Airtable CSV
csv = "export.csv"

# Der Ordner, in dem die Immatrikulationsbescheinigungen gespeichert werden sollen
imma_path = "immatrikulationsbescheinigungen"

# Der Ordner, in dem die Ergebnisse gespeichert werden sollen
output_pfad = "output"

# Die Studiengänge, die mit auf die Medis dürfen, genau so wie sie in der Immatrikulationsbescheinigung stehen
studiengaenge = ["Zahnmedizin", "Humanmedizin", "Medizin"]

# Die erlaubten Endungen der Emailadresse
erlaubte_email_domains = ["fau.de", "uni-erlangen.de"]

# Das aktuelle Semester wie in der Immatrikulationsbescheinigung.
# Falls es hier mehrere Möglichkeiten gibt, könnt ihr wie bei den Studiengängen
# eine Liste erstellen (also z. B. ["semester1", "semester2"]).
semester = ["Wintersemester 2022"]

# Die Spaltennamen, die ihr für das Airtable verwendet habt
vorname_spalte = "Vorname"
nachname_spalte = "Nachname"
email_spalte = "Email"
imma_bescheinigung_spalte = "Immatrikulationsbescheinigung"

# Das Geburtsdatum
# Falls diese Spalte leer ist (geburtsdatum_spalte = ""), wird nicht überprüft, ob jemand volljährig ist
geburtsdatum_spalte = "Geburtstag"
# Das Geburtsdatumsformat, wie es in den Immatrikulationsbescheinigungen steht.
# Falls euer Geburtsdatum anders aussieht als tt.mm.JJJJ könnt ihr es hier anpassen
geburtsdatum_format = "%d.%m.%Y"

# Der erste Tag der Medis (also der Tag, an dem die Leute Geburtstag haben müssen, um 18 zu sein)
medis_erster_tag = "08.06.2023"

# Die Regular Expression, die den Namen herausfiltert.
# Wendet euch bei Fragen an mich oder an den Informatiker eures Vertrauens
namen_regex = r"(?:Herr|Frau)\s+([A-zÀ-ú@0-9- üÜ]*),\s+(?:geboren|Matrikel-Nr.:)"

# Ab hier kommen Sachen die nur verändert werden sollten,
# wenn ihr wisst was ihr macht (oder neugierig seid)
# Das Regex für den Airtable Imma Upload
uploaded_imma_regex = "(.*) \((http[s].*)\)"

# Das Format des Geburtsdatums in Airtable
airtable_geburtstagsdatum_format = "%d/%m/%Y"

# Der maximale Levensthein Wert zum Namensvergleich
levensthein_cutoff = 66
