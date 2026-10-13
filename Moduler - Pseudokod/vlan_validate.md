    FUNKTION validera_konfiguration(konfig_filsökväg, ursprunglig_vlan_lista):
    Öppna 'konfig_filsökväg' och läs in all text till en variabel 'all_text'
    Skapa en tom lista för felmeddelanden som heter 'fel_rapport'
    
    # REGEL 1: Kontrollera SSH
    OM texten "transport input ssh" INTE finns i 'all_text':
        Lägg till i 'fel_rapport': "Regel 1 fel: SSH är inte aktiverat på vty-linjerna!"
        
    # REGEL 2: Kontrollera att alla VLAN från CSV finns med
    FÖR varje vlan i 'ursprunglig_vlan_lista':
        Skapa sökfrasen "vlan " + vlan["VLAN_ID"]
        OM sökfrasen INTE finns i 'all_text':
            Lägg till i 'fel_rapport': "Regel 2 fel: VLAN " + vlan["VLAN_ID"] + " saknas i konfigurationen!"
            
    # REGEL 3: Kontrollera osäkra lösenord
    OM texten "password cisco" finns i 'all_text':
        Lägg till i 'fel_rapport': "Regel 3 fel: Standardlösenordet 'cisco' används fortfarande!"
        
    SKICKA TILLBAKA 'fel_rapport'
