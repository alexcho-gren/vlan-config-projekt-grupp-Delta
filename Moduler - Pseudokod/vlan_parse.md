    FUNKTION läs_csv_fil(filsökväg):
    Skapa en tom lista som heter 'vlan_lista'
    
    Öppna filen på 'filsökväg' i läsläge
    Läs den första raden (rubrikerna) och hoppa över den
    
    FÖR varje rad som är kvar i filen:
        Dela upp raden vid varje kommatecken (så vi får ID, Namn, Beskrivning)
        Ta bort eventuella extra mellanslag eller tomma rader
        
        Skapa ett paket (t.ex. en dictionary) med:
            id = radens ID
            namn = radens Namn
            beskrivning = radens Beskrivning
            
        Lägg till detta paket i 'vlan_lista'
        
    Stäng filen
    SKICKA TILLBAKA 'vlan_lista'
