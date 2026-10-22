def generate_sw_config(vlans, sw_config_file):
    with open(sw_config_file, "w") as f:
        for vlan in vlans:
            f.write(f"vlan {vlan['VLAN_ID']}\n")
            f.write(f" name {vlan['VLAN_NAME']}\n")
            f.write("!\n")



if __name__ == "__main__":
    vlans = [
        {"VLAN_ID": 10, "VLAN_NAME": "Management"},
        {"VLAN_ID": 20, "VLAN_NAME": "Production"},
        {"VLAN_ID": 30, "VLAN_NAME": "Staff"},
        {"VLAN_ID": 40, "VLAN_NAME": "Guests"},
        {"VLAN_ID": 99, "VLAN_NAME": "Native"}
    ]
    sw_config_file = "switch_config.txt"

    generate_sw_config(vlans, sw_config_file)
    print("Switchkonfigurationen har sparats!")
