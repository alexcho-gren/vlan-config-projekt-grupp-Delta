# definierar funktionen "generate_r_config" och listan "vlan_data"
def generate_r_config(vlan_data):
    # Skapar och öppnar router.txt samt gör den skrivbar med "w"
    with open('router.txt', 'w') as f:
        aktiva_interface = []
        # för varje instans av vlan i vlan_data:
        for vlan in vlan_data:
            # variabler för vlan_data
            vlan_id = vlan['vlan_id']
            vlan_name = vlan['vlan_name']
            ip = vlan['ip_address']
            mask = vlan['subnet']
            enc1q = vlan['encapsulation_dot1q']
            iface_name = vlan['interface']
            if iface_name not in aktiva_interface:
                # skriver raden "interface" samt "no shutdown"
                f.write(f"interface {iface_name}\n")
                f.write(f" no shutdown\n") 
                f.write(f"!\n") 
                aktiva_interface.append(iface_name)
                # skriver raden och skapar subinterface på GigabitEthernet0/0
                f.write(f'interface {iface_name}.{vlan_id}\n')
                # skriver raden ip address + ip-nummer + subnätmask
                f.write(f'ip address {ip} {mask}\n')
                # skriver raden encapsulation dot1q + vlan-nummer
                f.write(f'encapsulation dot1q {enc1q}\n')
                # lägger till beskrivning för interfacet
                f.write(f'description Gateway for {vlan_name}\n')
                # för struktur i utdatan
                f.write(f'!\n')
            # returnerar router.txt med de skrivna raderna i
            return open('router.txt')
    
# Exempellista på data att ställa upp för routerkonfig
if __name__ == "__main__":
    vlan_data = [
        {'vlan_id': 10, 'vlan_name': 'Management', 'description': 'None', 'ip_address': '192.168.1.1', 'subnet': '255.255.255.192', 'interface': 'GigabitEthernet0/0', 'encapsulation_dot1q': 10},
        {'vlan_id': 20, 'vlan_name': 'Production', 'description': 'None', 'ip_address': '192.168.1.65', 'subnet': '255.255.255.192', 'interface': 'GigabitEthernet0/0', 'encapsulation_dot1q': 20},
        {'vlan_id': 30, 'vlan_name': 'Staff', 'description': 'None', 'ip_address': '192.168.1.129', 'subnet': '255.255.255.192', 'interface': 'GigabitEthernet0/0', 'encapsulation_dot1q': 30},
        {'vlan_id': 40, 'vlan_name': 'Guests', 'description': 'None', 'ip_address': '192.168.1.193', 'subnet': '255.255.255.192', 'interface': 'GigabitEthernet0/0', 'encapsulation_dot1q': 40}
    ]
    
    # Skriver resultatet av generate_r_config(vlan_data) till "router.txt". 
    # Den här delen av funktionen har jag hämtat från Ragheds funktion (vlan_generate). Utan den skapades inte "router.txt".
    resultat = generate_r_config(vlan_data)
    print(resultat)

    #***DISCLAIMER*** 
    # 
    #   Mistral har hjälpt mig får rätt på write-raderna, 
    #   jag hade inte använt parenteser för att stänga in raden.
    #   
    #   Print-raderna har jag hämtat från Ragheds (vlan_generate), 
    #   utan den skapades inte "router.txt".
    #   
    #   Alexander (main.py) hjälpte mig använda variabler ur 
    #   vlan_data istället för att behöva skriva ut värdena på varje f.write-rad
    #   samt sett till att raden med no shutdown bara skrivs en gång, med mera.
