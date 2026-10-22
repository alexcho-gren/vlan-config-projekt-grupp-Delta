# Definierar funktionen som tar emot listan med data samt namnet på filen som skapas
def generate_sw_config(vlan_data, sw_config_file):

    # Öppnar textfil i skrivläge ('w')
    with open(sw_config_file, "w") as f:

        # Loopar igenom listan rad för rad, ett VLAN i taget
        for vlan in vlan_data:

            # Skriver kommandot 'vlan ' följt av aktuellt ID-nummer från listan till filen
            f.write(f"vlan {vlan['vlan_id']}\n")

            # Kontrollerar om nyckeln 'vlan_name' innehåller ett namn (inte en tom sträng)
            if vlan['vlan_name']:
                # Om namnet finns skrivs kommandot ' name' följt av VLAN-namnet till filen
                f.write(f" name {vlan['vlan_name']}\n")
            # Skriver ett avslutande utropstecken till filen
            f.write("!\n")

