import csv

def read_csv_file(filename):
    vlan_list = []

    with open(filename, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            vlan_list.append(row)

    return vlan_list