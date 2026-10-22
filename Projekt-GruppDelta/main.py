# Importerar modul som gör att programmet kan prata direkt med datorns Operativ System
import os

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
    
    # Modulär inmatning av CSV-fil
    user_input = input("Ange sökväg till CSV-fil (Tryck Enter för standard 'vlan_data.csv'): ")
    # OM inmatning INTE är "" (Enter)
    if user_input.strip() != "":
        # Så är csv_file = <inmatad sökväg>
        csv_file = user_input.strip()

    # ANNARS:
    else:
        # Så är csv_file = "vlan_data.csv"
        csv_file = "vlan_data.csv"

    # Frågar Operativ Systemet om sökvägen för csv_file finns

    # OM sökväg INTE finns:
    if not os.path.exists(csv_file):
        # Skriv ut felmeddelande
        print(f"\n[FEL] Det gick inte att starta programmet.")
        print(f"Orsak: Hittade inte filen '{csv_file}'. Kontrollera stavningen och att filen ligger i rätt mapp.")
        
        # Avbryt main() med return
        print("Programmet avslutas.")
        return

    # Variabel med namnet på switchens konfig-fil
    sw_config_file = "switch_config.txt"
    # Variabel med namnet på routerns konfig-fil
    r_config_file = "router_config.txt"
    
    # Anropar parse-funktionen och sparar listan den returnerar i 'vlan_list'
    # Skriver ut meddelande till terminalen
    print("=== Startar nätverkskonfigurering och validering ===")
    vlan_list = read_csv_file(csv_file)

    # Skickar listan och switch-filnamnet till vlan_generate
    # Skriver ut meddelande till terminalen
    print(f"[2/4] Genererar switch-konfiguration: {sw_config_file}...")
    generate_sw_config(vlan_list, sw_config_file)

    # Skickar listan och router-filnamnet till router_generate
    # Skriver ut meddelande till terminalen
    print(f"[3/4] Genererar router-konfiguration: {r_config_file}...")
    generate_r_config(vlan_list, r_config_file)

    # Skickar switch-konfig till validering och sparar svaret (True/False)
    # Skickar router-konfig till validering och sparar svaret (True/False)
    # Skriver ut meddelande till terminalen
    print("[4/4] Validerar de genererade filerna mot reglerna...")
    sw_is_valid = validate_config(sw_config_file)
    r_is_valid = validate_config(r_config_file)

    # Kontrollerar om BÅDE switch-filen och router-filen blev godkända
    if sw_is_valid and r_is_valid:

        # Om båda variablerna är True, så skrivs det ut som godkänt i terminalen
        print("Status: Godkänd. Alla konfigurationer uppfyller kraven.")

    # Om en eller båda är False, så körs detta block istället
    else:

        #Skriver ut "Icke godkänd." i terminalen
        print("Status: Icke godkänd. Ett eller flera regelbrott upptäcktes.")

# Kontrollerar att just denna fil startades direkt av användaren i terminalen
if __name__ == "__main__":

    # Om filen kördes direkt, så anropas funktionen main(), som startar flödet
    main()