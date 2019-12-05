import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')


def compute_mass(mass):
    return int((mass/3)) - 2

result = 0
for line in file.readlines():
    result += compute_mass(int(line))

print("Needed fuel : ")
print(result)
