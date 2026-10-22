# Importerar modul som hanterar CSV-filer
import csv

# Definierar funktion som tar emot sökväg för CSV-fil som ska läsas
def read_csv_file(filename):

    # Skapar en tom lista där alla rader från CSV-tabellen sparas (ordlistor)
    vlan_list = []

    # Öppnar CSV-filen i läsläge ('r'), sätter teckenkodning till utf-8, rensar radbrytning
    with open(filename, "r", encoding="utf-8", newline="") as csv_file:

        # DictReader läser varje rubrikrad i CSV-filen (den allra första raden) och katergoriserar
        # varje rubrik med raderna under rubriken. Skapar en dict för varje rubrik automatiskt
        reader = csv.DictReader(csv_file)

        # for-loop som appendar varje rad i listan ovan
        for row in reader:
            vlan_list.append(row)
    
    # Returnerar den färdiga listan efter filen har lästs
    return vlan_list