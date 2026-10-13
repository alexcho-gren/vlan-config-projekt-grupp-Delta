    FUNKTION generera_cli_konfig(vlan_lista):
    Skapa en tom textsträng som heter 'switch_text'
    Lägg till en startkommentar: "! --- Switch VLAN Konfiguration ---"
    
    FÖR varje vlan i 'vlan_lista':
        Skapa textraden: "vlan " + vlan["VLAN_ID"]
        Lägg till textraden i 'switch_text'
        
        Skapa textraden: " name " + vlan["VLAN_Name"]
        Lägg till textraden i 'switch_text'
        
        Skapa textraden: " description " + vlan["Description"]
        Lägg till textraden i 'switch_text'
        
        Lägg till en tom rad och ett utropstecken "!" för struktur
        
    SKICKA TILLBAKA 'switch_text'
