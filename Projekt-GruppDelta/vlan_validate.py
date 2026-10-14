def validate_config(filename):

    fel_rapport = []

    with open(filename, "r") as file:

        lines = file.readlines()

    current_vlan = None

    for line in lines:

        line = line.strip()

        if line == "vlan 1":

            current_vlan = 1

        elif line.startswith("vlan "):

            current_vlan = int(line.split()[1])

        elif line == "!" or line == "exit":

            current_vlan = None

        if current_vlan == 1 and line.startswith("name "):

            fel_rapport.append("Regel 1 fel: VLAN 1 får inte ha ett namn!")
        # Regel 2: Inga lösenord

        if "password" in line.lower() or "secret" in line.lower():

            fel_rapport.append(

                "Regel 2 fel: Lösenord hittades i konfigurationen!"

            )
        # Regel 3: VLAN-namn max 32 tecken

        if current_vlan is not None and line.startswith("name "):
            vlan_name = line[5:]

            if len(vlan_name) > 32:
                fel_rapport.append("Regel 3 fel: VLAN-namet ät för långt!")
  
    return fel_rapport

