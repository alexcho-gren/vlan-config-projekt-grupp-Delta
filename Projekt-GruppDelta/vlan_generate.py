def generate_sw_config(vlan_data, sw_config_file):
    with open(sw_config_file, "w") as f:
        for vlan in vlan_data:
            f.write(f"vlan {vlan['vlan_id']}\n")
            if vlan['vlan_name']:
                f.write(f" name {vlan['vlan_name']}\n")
            f.write("!\n")

