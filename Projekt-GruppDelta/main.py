# Hämtar funktionen som läser CSV-filen från modul vlan_parse
from vlan_parse import read_csv_file

# Hämtar funktionen som skapar switch-konfigurationen från modulen vlan_generate
from vlan_generate import generate_sw_config

# Hämtar funktionen som skapar router-konfigurationen från modulen router_generate
from router_generate import generate_r_config

# Hämtar funktionen som granskar reglerna från modulen vlan_validate
from vlan_validate import validate_config


# Huvudfunktionen - Definerar programflödet
def main():
    
    # Variabel som sparar namnet på CSV-filen som ska läsas in
    csv_file = "vlan_data.csv"

    # Variabel med namnet på switchens konfig-fil
    sw_config_file = "switch_config.txt"

    # Variabel med namnet på routerns konfig-fil
    r_config_file = "router_config.txt"

    # Anropar parse-funktionen och sparar listan den returnerar i 'vlan_list'
    vlan_list = read_csv_file(csv_file)

    # Skickar listan och switch-filnamnet till vlan_generate
    generate_sw_config(vlan_list, sw_config_file)

    # Skickar listan och router-filnamnet till router_generate
    generate_r_config(vlan_list, r_config_file)

    # Skickar switch-konfig till validering och sparar svaret (True/False)
    sw_is_valid = validate_config(sw_config_file)

    # Skickar router-konfig till validering och sparar svaret (True/False)
    r_is_valid = validate_config(r_config_file)

    # Kontrollerar om BÅDE switch filen och router-filen blev godkända
    if sw_is_valid and r_is_valid:

        # Om båda variablerna är True, så skrivs det ut som godkänt i terminalen
        print("Godkänd.")

    # Om en eller båda är False, så körs detta block istället
    else:

        #Skriver ut "Icke godkänd." i terminalen
        print("Icke godkänd.")

# Kontrollerar att just denna fil startades direkt av användaren i terminalen
if __name__ == "__main__":

    # Om filen kördes direkt, så anropas funktionen main(), som startar flödet
    main()