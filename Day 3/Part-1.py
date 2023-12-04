
if __name__ == "__main__":
    with open("Input.txt") as f:
        schematic = []
        line_number = 0
        for line in f:
            schematic.append([])
            for char in line:
                schematic[line_number].append(char)
            line_number += 1

        part_number_sum = 0
        current_number = ""
        is_valid_number = False
        in_number = False
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
                            if not schematic[x][y].isnumeric() and not schematic[x][y] == ".":
                                is_valid_number = True
                else:
                    in_number = False
                    if is_valid_number:
                        is_valid_number = False
                        part_number_sum += int(current_number)
        
        print(part_number_sum)
