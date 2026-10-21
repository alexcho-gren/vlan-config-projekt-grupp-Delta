# definierar funktionen "generate_r_config" och listan "vlan_data"
def generate_r_config(vlan_data):
    
    # Skapar och öppnar router.txt samt gör den skrivbar med "w"
    with open('router.txt', 'w') as f:
        # för varje instans av vlan i vlan_data:
        for vlan in vlan_data:
            # skriver raden "interface" samt "no shutdown"
            f.write(f'interface {vlan["interface"]} no shutdown\n')
            # skriver raden och skapar subinterface på GigabitEthernet0/0
            f.write(f'interface GigabitEthernet0/0.{vlan["vlan_id"]}\n')
            # skriver raden ip address + ip-nummer + subnätmask
            f.write(f'ip address {vlan["ip_address"]} {vlan["subnet"]}\n')
            # skriver raden encapsulation dot1q + vlan-nummer
            f.write(f'encapsulation dot1q {vlan["encapsulation_dot1q"]}\n')
            # lägger till beskrivning för interfacet
            f.write(f'description Gateway for {vlan["vlan_name"]}\n')
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

    #***AI DISCLAIMER*** 
    # 
    #   Mistral har hjälpt mig får rätt på write-raderna: 
    #   Jag skrev f.write(rad);f'interface {interface} + no shutdown\n' 
    #   vilket Mistral visade uppmärksammade mig på att ändra till 
    #   f.write(f'interface {vlan["interface"]} no shutdown\n') 
    #   eftersom funktionen write aldrig kallades på. 
    # 
    #   Dessutom var mina defintioner av listobjekten fel, 
    #   vilken jag fick ändra på alla write-rader, 
    #   vilket i sin tur resulterade i att jag kunde #mina onödiga defintioner (se nedan).
        
        #interface = rad ('interface')
        #vl_id = rad['vlan_id']
        #vlan_name = rad['vlan_name']
        #enc1q = rad['encapsulation_dot1q']
        #ip = rad['ip_address']
        #subn = rad['subnet']

    #   Till sist visade Mistral att jag skapade en dictionary i varje instans vilket "skuggade" variablerna i exempellistan.