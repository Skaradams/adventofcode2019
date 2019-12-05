import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')


def compute_mass(mass):
    return int((mass/3)) - 2

# Part 1
fuel = 0
for line in file.readlines():
    fuel += compute_mass(int(line))

print("Needed fuel for modules : ")
print(fuel)


# Part 2
result = fuel
needed_fuel = 0
while fuel > 0:
    fuel = compute_mass(fuel)
    needed_fuel += fuel
    if(fuel > 0):
        result += fuel

print("Needed fuel for modules and fuel : ")
print(result)
