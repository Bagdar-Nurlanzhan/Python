import json
json_file_path = "C:\\Users\\tursy\\OneDrive\\Рабочий стол\\python\\Python\\lab4\\json\\sample-data.json"

with open(json_file_path, "r") as file:
    data = json.load(file)
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)
required_interfaces = {"eth1/33", "eth1/34", "eth1/35"}

for item in data["imdata"]:
    interface = item.get("l1PhysIf", {}).get("attributes", {})
    dn = interface.get("dn", "N/A")

    # Егер DN ішінде қажетті интерфейстердің бірі болса, шығарамыз
    if any(iface in dn for iface in required_interfaces):
        descr = interface.get("descr", "")
        speed = interface.get("speed", "inherit")
        mtu = interface.get("mtu", "N/A")
        print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")