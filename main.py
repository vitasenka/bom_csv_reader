from csv import DictReader


def calculate_costs(bom_data):
    costs = {}
    for part in bom_data:
        try:
            field_name = "part_name"
            if not part[field_name].strip():
                print("The name of the part can not be empty.")
                continue
            field_name = "material"
            if not part[field_name].strip():
                print(f"Empty material is not allowed for {part['part_name']}.")
                continue
            field_name = "quantity"
            part["quantity"] = int(part["quantity"])
            if invalid_range(part, field_name):
                continue
            field_name = "unit_cost"
            part["unit_cost"] = float(part["unit_cost"])
            if invalid_range(part, field_name):
                continue

        except ValueError:
            if not part[field_name].strip():
                message = f"The {field_name} is missing for part: {part['part_name']}."
            else:
                message = f"The value of {field_name} is not valid ({part[field_name]!r}) for part: {part['part_name']}."
            print(message)
            continue
        name = part["part_name"]
        costs[name] = part["quantity"] * part["unit_cost"]
        costs["total"] = costs.get("total", 0.0) + costs[name]
        material = part["material"]
        costs[material] = costs.get(material, 0.0) + costs[name]
    return costs


def invalid_range(part, field_name):
    value = part[field_name]
    criteria = 1 if field_name == "quantity" else 0.0
    if value < criteria:
        print(
            f"The value of {field_name} can not be lower than {criteria} ({value!r}) for part: {part['part_name']}."
        )
        return True
    return False


def print_costs(costs):
    for part_name, cost in costs.items():
        print(part_name, f"cost: ${cost:.2f}")


with open("bom.csv", newline="") as csvfile:
    bom_data = DictReader(csvfile)
    costs = calculate_costs(bom_data)
    print_costs(costs)
