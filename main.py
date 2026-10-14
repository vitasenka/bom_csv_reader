from csv import DictReader


def calculate_costs(bom_data):
    costs = {}
    for part in bom_data:
        part["quantity"] = int(part["quantity"])
        part["unit_cost"] = float(part["unit_cost"])
        name = part["part_name"]
        costs[name] = part["quantity"] * part["unit_cost"]
        costs["total"] = costs.get("total", 0.0) + costs[name]
        material = part["material"]
        costs[material] = costs.get(material, 0.0) + costs[name]
    return costs


def print_costs(costs):
    for part_name, cost in costs.items():
        print(part_name, f"cost: ${cost:.2f}")


with open("bom.csv", newline="") as csvfile:
    bom_data = DictReader(csvfile)
    costs = calculate_costs(bom_data)
    print_costs(costs)
