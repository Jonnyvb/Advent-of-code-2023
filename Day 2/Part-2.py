
if __name__ == "__main__":
    with open("Input.txt") as f:
        game_power_sum = 0
        game_number = 0
        for line in f:
            game_number += 1
            draws = line.split(":")[1].strip().split(";")
            max_red = 0
            max_green = 0
            max_blue = 0
            for draw in draws:
                cubes = draw.strip().split(",")
                for cube in cubes:
                    count = int(cube.strip().split(" ")[0])
                    colour = cube.strip().split(" ")[1]
                    if colour == "red" and count > max_red:
                        max_red = count
                    elif colour == "green" and count > max_green:
                        max_green = count
                    elif colour == "blue" and count > max_blue:
                        max_blue = count
            
            game_power = max_red * max_green * max_blue
            game_power_sum += game_power
        
        print(game_power_sum)