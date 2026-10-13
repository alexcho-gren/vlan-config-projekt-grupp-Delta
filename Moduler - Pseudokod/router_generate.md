    FUNKTION generera_router_konfig(vlan_lista, fysiskt_interface):
    Skapa en tom textsträng som heter 'router_text'
    Lägg till en startkommentar: "! --- Router Sub-interfaces ---"
    
    FÖR varje vlan i 'vlan_lista':
        # Skapa sub-interfacet (t.ex. interface GigabitEthernet0/0.10)
        Skapa textraden: "interface " + fysiskt_interface + "." + vlan["VLAN_ID"]
        Lägg till i 'router_text'
        
        # Slå på dot1Q-inkapsling för rätt VLAN
        Skapa textraden: " encapsulation dot1Q " + vlan["VLAN_ID"]
        Lägg till i 'router_text'
        
        # Lägg till beskrivning
        Skapa textraden: " description Gateway for " + vlan["VLAN_Name"]
        Lägg till i 'router_text'
        
        Lägg till en tom rad och ett utropstecken "!" för struktur
        
    SKICKA TILLBAKA 'router_text'
