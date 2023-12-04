
def word_to_number(word: str) -> str:
    if word[:3] == "one":
        return "1"
    elif word[:3] == "two":
        return "2"
    elif word[:5] == "three":
        return "3"
    elif word[:4] == "four":
        return "4"
    elif word[:4] == "five":
        return "5"
    elif word[:3] == "six":
        return "6"
    elif word[:5] == "seven":
        return "7"
    elif word[:5] == "eight":
        return "8"
    elif word[:4] == "nine":
        return "9"
    else:
        return False

import os

if __name__ == "__main__":
    print(os.getcwd())
    with open("Input.txt") as f:
        calibration_value_sum = 0
        for line in f:
            first_digit = False
            last_digit = False
            for i in range(len(line)):
                if line[i:i+1].isnumeric():
                    first_digit = line[i:i+1]
                    break
                first_digit = word_to_number(line[i:])
                if first_digit:
                    break
            for i in range(len(line)):
                if line[-(i + 1):-i].isnumeric():
                    last_digit = line[-(i + 1):-i]
                    break
                last_digit = word_to_number(line[-(i + 1):])
                if last_digit:
                    break
            
            calibration_value = first_digit + last_digit
            calibration_value_sum += int(calibration_value)

        print(calibration_value_sum)