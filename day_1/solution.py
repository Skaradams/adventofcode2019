import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))



def compute_mass(mass):
    return int((mass/3)) - 2

# Part 1
fuel = 0
file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')
for line in file.readlines():
    fuel += compute_mass(int(line))

print("Needed fuel for modules : ")
print(fuel)


# Part 2
def compute_mass_with_fuel(mass):
    fuel = compute_mass(mass)
    result = fuel
    while fuel > 0:
        fuel = compute_mass(fuel)
        if(fuel > 0):
            result += fuel
    return result

fuel = 0
file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')
for line in file.readlines():
    fuel += compute_mass_with_fuel(int(line))

print("Needed fuel for modules and fuel : ")
print(fuel)
