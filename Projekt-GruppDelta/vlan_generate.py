def generate_sw_config(vlan_data, sw_config_file):
    with open(sw_config_file, "w") as f:
        for vlan in vlan_data:
            f.write(f"vlan {vlan['vlan_id']}\n")
            f.write(f" name {vlan['vlan_name']}\n")
            f.write("!\n")



if __name__ == "__main__":
    vlans = [
        {"vlan_id": 10, "vlan_name": "Management"},
        {"vlan_id": 20, "vlan_name": "Production"},
        {"vlan_id": 30, "vlan_name": "Staff"},
        {"vlan_id": 40, "vlan_name": "Guests"},
        {"vlan_id": 99, "vlan_name": "Native"}
    ]
    sw_config_file = "switch_config.txt"

    generate_sw_config(vlans, sw_config_file)
    print("Switchkonfigurationen har sparats!")
