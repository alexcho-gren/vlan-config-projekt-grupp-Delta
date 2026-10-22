# definierar funktionen "generate_r_config" och listan "vlan_data"
def generate_r_config(vlan_data, r_config_file):
    # Skapar och öppnar textfil, samt gör den skrivbar med "w"
    with open(r_config_file, 'w') as f:
        aktiva_interface = []
        # för varje instans av vlan i vlan_data:
        for vlan in vlan_data:
            # variabler för vlan_data
            vlan_id = vlan['vlan_id']
            vlan_name = vlan['vlan_name']
            ip = vlan['ip_address']
            mask = vlan['subnet']
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
            f.write(f' encapsulation dot1q {vlan_id}\n')
            # lägger till beskrivning för interfacet
            f.write(f'description Gateway for {vlan_name}\n')
            # för struktur i utdatan
            f.write(f'!\n')


#***DISCLAIMER***
#   Mistral har hjälpt mig får rätt på write-raderna, 
#   jag hade inte använt parenteser för att stänga in raden.
#   Alexander (main.py) hjälpte mig använda variabler ur 
#   vlan_data istället för att behöva skriva ut värdena på varje f.write-rad
#   samt sett till att raden med no shutdown bara skrivs en gång, med mera.