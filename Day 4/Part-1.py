
if __name__ == "__main__":
    with open("Input.txt") as f:
        total_points = 0
        for line in f:
            _, numbers = line.split(":")
            winning_numbers, our_numbers = numbers.strip().split("|")
            winning_numbers = winning_numbers.strip().replace("  ", " ").split(" ")
            our_numbers = our_numbers.strip().replace("  ", " ").split(" ")
            match_count = len(set(winning_numbers).intersection(set(our_numbers)))
            if match_count == 0:
                continue
            else:
                points = 2**(match_count-1)
                total_points += points

        print(total_points)