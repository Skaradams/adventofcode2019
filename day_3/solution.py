import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')
lines = file.readlines()

cable1 = lines[0].split(",")
cable2 = lines[1].split(",")


def parse_instruction(instruction):
    return (instruction[0], int(instruction[1:]))


def get_coordinates(instructions, other_coordinates=None):
    coordinates = [[0, 0]]
    intersections = []

    for instruction in instructions:
        instruction_data = parse_instruction(instruction)
        origin = coordinates[len(coordinates) - 1]
        new_coordinates = (0,0)
        for i in range(instruction_data[1]):
            if(instruction_data[0] == 'R'):
                new_coordinates = (
                    origin[0] + i,
                    origin[1]
                )
            elif(instruction_data[0] == 'L'):
                new_coordinates = (
                    origin[0] - i,
                    origin[1]
                )
            elif(instruction_data[0] == 'U'):
                new_coordinates = (
                    origin[0],
                    origin[1] + i
                )
            elif(instruction_data[0] == 'D'):
                new_coordinates = (
                    origin[0],
                    origin[1] - i
                )
        coordinates.append(new_coordinates)

        if(other_coordinates and new_coordinates in other_coordinates):
            print("qsdhgqsjdhq")
            intersections.append(new_coordinates)

    return (coordinates, intersections)

def compare_coordinates(coordinates1, coordinates2):
    common_coordinates = []

    for coordinate in coordinates2:
        if(coordinate in coordinates1):
            common_coordinates.append(coordinate)
    return common_coordinates


(a, intersections) = get_coordinates(cable1)
(b, intersections) = get_coordinates(cable2, a)

print(intersections)
