# Definition av funktionen som tar emot namnet på den fil som ska granskas
def validate_config(filename):
    
    # Skapar en flagga som vi utgår från är True tills ett fel hittas
    is_valid = True
    
    # Skapar en strömbrytare ("kom-ihåg-flagga") för VLAN 1 och sätter den till False från början
    vlan_1_aktiv = False

    # Öppnar textfilen (konfigurationen) i läsläge ('r' för read)
    with open(filename, "r") as file:
        
        # Startar en loop som läser igenom textfilen rad för rad, uppifrån och ner
        for line in file:
            
            # Rensar bort dolda radbrytningar (\n) och extra mellanslag i början/slutet av raden
            line = line.strip()

            # --- DEL 1: HÅLL KOLL PÅ VILKET VLAN VI ÄR I (STRÖMBRYTAREN) ---
            
            # Kontrollerar OM textraden är exakt "vlan 1"
            if line == "vlan 1":
                # OM det är VLAN 1, slås strömbrytaren PÅ (sätts till True)
                vlan_1_aktiv = True
                
            # Kontrollerar OM raden startar med ordet "vlan " OCH att den INTE är vlan 1

            # OM raden startar med "vlan " OCH raden INTE är "vlan 1":
            if line.startswith("vlan ") and line != "vlan 1":
                # Så är vi på ett annat VLAN-nummer, strömbrytaren slås AV (sätts till False)
                vlan_1_aktiv = False
                
            # Kontrollerar OM raden är ett utropstecken ELLER ordet "exit" (blocket avslutas)
            if line == "!" or line == "exit":
                # Om vi går ur VLAN-konfigureringen helt, slår strömbrytaren också AV
                vlan_1_aktiv = False

            # --- DEL 2: GRANSKA DE TRE REGLERNA ---
            
            # KONTROLL: Regel 1 & Regel 3 (Körs bara om raden faktiskt sätter ett namn)
            
            # OM raden BÖRJAR med "name ":
            if line.startswith("name "):
                
                # Klipper bort ordet "name " (de första 5 tecknen) så att bara själva namnet sparas
                # Mellanslaget efter "name" räknas som ett tecken
                vlan_name = line[5:].strip()

                # REGEL 1: Kontrollerar OM strömbrytaren för VLAN 1 är PÅ (True)

                # OM flaggan är PÅ:
                if vlan_1_aktiv == True:
                    # Så har VLAN 1 fått ett namn, vilket är ett regelbrott
                    print(f"[FEL] Regel 1 bruten: VLAN 1 har fått ett namn ('{vlan_name}')!")
                    # Programmets status sätts till False eftersom filen är underkänd
                    is_valid = False

                # REGEL 3: Kontrollerar om namnet består av fler än 32 tecken

                # OM värdet i 'vlan_name' är är HÖGRE än 32:
                if len(vlan_name) > 32:
                    # Är namnet för långt, skriv ut ett felmeddelande i terminalen
                    print(f"[FEL] Regel 3 bruten: Namnet '{vlan_name}' är för långt ({len(vlan_name)} tecken)!")
                    # Programmets status sätts till False
                    is_valid = False

            # REGEL 2: Kontrollerar om känsliga lösenordsord finns i textraden
            # .lower() gör om hela raden till små bokstäver så vi inte missar ord som "Secret" eller "PASSWORD"

            # OM "password" FINNS I raden ELLER "secret" FINNS I raden:
            if "password" in line.lower() or "secret" in line.lower():
                # Så skrivs raden där felet fanns ut i terminalen
                print(f"[FEL] Regel 2 bruten: Hittade ett lösenord i raden: '{line}'")
                # Programmets status sätts till False
                is_valid = False

    # När hela filen är färdigläst skickar vi tillbaka om filen var godkänd (True) eller underkänd (False)
    return is_valid
