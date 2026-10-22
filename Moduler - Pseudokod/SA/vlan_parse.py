import csv

def read_csv_file(filename):
    vlan = []

    with open(filename, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            vlan.append(row)

    return vlan


vlans = read_csv_file("Moduler - Pseudokod/SA/test.csv")
print(vlans) 