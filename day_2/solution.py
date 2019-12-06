import os

# Lecture du fichier d'inputs
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# liste des valeurs
opcode = 0
position1 = 1
position2 = 2
result_position = 3

def reset_memory():
    file = open(os.path.join(THIS_FOLDER, "input.txt"), 'r')
    line = file.readlines()[0]
    return list(map(lambda number: int(number), line.split(",")))

def get_position(values, position_index):
    return(values[values[position_index]])

# Fonction qui process la liste
def process_list(values, opcode, position1, position2, result_position, coef=0):

    [current_opcode, current_position1, current_position2, current_result_position] = list(map(
        lambda num: num + 4 * coef,
        [opcode, position1, position2, result_position]
    ))

    # Ici nous faisons des additions et des multiplications
    if(values[current_opcode] == 1):
        values[values[current_result_position]] = get_position(values, current_position1) + get_position(values, current_position2)

        return(
            process_list(values, opcode, position1, position2, result_position, coef + 1)
        )
    elif(values[current_opcode] == 2):
        values[values[current_result_position]] = get_position(values, current_position1) * get_position(values, current_position2)
        return(
            process_list(values, opcode, position1, position2, result_position, coef + 1)
        )
    elif(values[current_opcode] == 99):
        return values
    else:
        # affiche "ça pue à l'écran"
        print("ça pue")
        return values


# Part 1
values = reset_memory()
values[1] = 12
values[2] = 2
print("First solution :")
print(process_list(values, opcode, position1, position2, result_position))


# Part 2

expected_value = 19690720
result = 0
for noun in range(100):
    for verb in range(100):
        values = reset_memory()
        values[1] = noun
        values[2] = verb
        if(process_list(values, opcode, position1, position2, result_position)[0] == expected_value):
            result = 100 * noun + verb


print("Second solution :")
print(result)
