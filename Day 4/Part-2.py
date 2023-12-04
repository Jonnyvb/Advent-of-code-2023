
if __name__ == "__main__":
    with open("Input.txt") as f:
        scratch_card_tallies = {}
        scratch_card_number = 0
        for line in f:
            scratch_card_number += 1
            if not scratch_card_number in scratch_card_tallies:
                scratch_card_tallies[scratch_card_number] = 1
            else:
                scratch_card_tallies[scratch_card_number] += 1

            _, numbers = line.split(":")
            winning_numbers, our_numbers = numbers.strip().split("|")
            winning_numbers = winning_numbers.strip().replace("  ", " ").split(" ")
            our_numbers = our_numbers.strip().replace("  ", " ").split(" ")
            match_count = len(set(winning_numbers).intersection(set(our_numbers)))
            if match_count == 0:
                continue
            else:
                for i in range(scratch_card_number+1, scratch_card_number+match_count+1):
                    if not i in scratch_card_tallies:
                        scratch_card_tallies[i] = 0
                    scratch_card_tallies[i] += scratch_card_tallies[scratch_card_number]

        scratch_card_count = 0
        for card_number, count in scratch_card_tallies.items():
            if card_number > scratch_card_number:
                break
            scratch_card_count += count

        print(scratch_card_count)