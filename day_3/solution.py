import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')
lines = file.readlines()

cable1 = lines[0].split(",")
cable2 = lines[1].split(",")


def parse_instruction(instruction):
    return (instruction[0], int(instruction[1:]))

def get_coordinates(instructions):
    coordinates = [[0, 0]]
    print('get coordinates')
    for instruction in instructions:
        instruction_data = parse_instruction(instruction)
        origin = coordinates[len(coordinates) - 1]

        for i in range(instruction_data[1]):
            if(instruction_data[0] == 'R'):
                coordinates.append([
                    origin[0] + i,
                    origin[1]
                ])
            elif(instruction_data[0] == 'L'):
                coordinates.append([
                    origin[0] - i,
                    origin[1]
                ])
            elif(instruction_data[0] == 'U'):
                coordinates.append([
                    origin[0],
                    origin[1] + i
                ])
            elif(instruction_data[0] == 'D'):
                coordinates.append([
                    origin[0],
                    origin[1] - i
                ])

    return coordinates

def compare_coordinates(coordinates1, coordinates2):
    common_coordinates = []
    for coordinate in coordinates2:
        if(coordinate in coordinates1):
            common_coordinates.append(coordinate)
    return common_coordinates

print(compare_coordinates(
    get_coordinates(cable1),
    get_coordinates(cable2),
))
