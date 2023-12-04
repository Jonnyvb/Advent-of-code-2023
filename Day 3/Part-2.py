
if __name__ == "__main__":
    with open("Input.txt") as f:
        schematic = []
        line_number = 0
        for line in f:
            schematic.append([])
            for char in line:
                schematic[line_number].append(char)
            line_number += 1

        current_number = ""
        number_gears = set()
        in_number = False
        is_valid_number = False
        gear_numbers = {}
        for i, row in enumerate(schematic):
            for j, char in enumerate(row):
                if char.isnumeric():
                    if in_number:
                        current_number += char
                    else:
                        current_number = char
                        in_number = True

                    coords_to_check = set()
                    coords_to_check.add((i-1, j-1))
                    coords_to_check.add((i,   j-1))
                    coords_to_check.add((i+1, j-1))
                    coords_to_check.add((i-1, j))
                    coords_to_check.add((i+1, j))
                    coords_to_check.add((i-1, j+1))
                    coords_to_check.add((i,   j+1))
                    coords_to_check.add((i+1, j+1))

                    for x, y in coords_to_check:
                        if x > 0 and x < len(row) and y > 0 and y < len(schematic):
                            if schematic[x][y] == "*":
                                number_gears.add((x,y))
                                is_valid_number = True
                else:
                    in_number = False
                    if is_valid_number:
                        for gear in number_gears:
                            if not gear in gear_numbers:
                                gear_numbers[gear] = []
                            gear_numbers[gear].append(int(current_number))
                        is_valid_number = False
                        number_gears = set()
        gear_ratio_sum = 0
        for gear, numbers in gear_numbers.items():
            if len(numbers) == 2:
                gear_ratio = 1
                for number in numbers:
                    gear_ratio *= number
                gear_ratio_sum += gear_ratio
        print(gear_ratio_sum)
