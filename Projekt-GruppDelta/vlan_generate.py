def generate_sw_config(vlans):
    config = ""

    for vlan in vlans:
        config += f"vlan {vlan['VLAN_ID']}\n"
        config += f" name {vlan['VLAN_NAME']}\n"
        config += "!\n"

    return config

if __name__ == "__main__":
    vlans = [
        {"VLAN_ID": 10, "VLAN_NAME": "Management"},
        {"VLAN_ID": 20, "VLAN_NAME": "Production"},
        {"VLAN_ID": 30, "VLAN_NAME": "Staff"},
        {"VLAN_ID": 40, "VLAN_NAME": "Guests"},
        {"VLAN_ID": 99, "VLAN_NAME": "Native"}
    ]
    resultat = generate_sw_config(vlans)
    print(resultat)