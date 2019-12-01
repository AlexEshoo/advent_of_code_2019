# PART I
def calculate_fuel_required(mass):
    return int(mass / 3) - 2

with open('input/input_day01_01.txt', 'r') as f:
    module_masses = [int(line) for line in f]

fuel_counter_upper = (calculate_fuel_required(m) for m in module_masses)

print(f"The total fuel required is: {sum(fuel_counter_upper)}")

# PART II
def recursive_fuel_calc(mass):
    if (fuel := int(mass / 3) - 2) > 0:
        return fuel + recursive_fuel_calc(fuel)
    else:
        return 0

fuel_counter_upper = (recursive_fuel_calc(m) for m in module_masses)

print(f"The Corrected Total Fuel Requied is: {sum(fuel_counter_upper)}")