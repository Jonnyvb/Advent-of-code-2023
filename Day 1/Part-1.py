
if __name__ == "__main__":
    with open("Input.txt") as f:
        calibration_value_sum = 0
        for line in f:
            first_digit = ""
            last_digit = ""
            for char in line:
                if char.isnumeric():
                    first_digit = char
                    break
            for char in reversed(line):
                if char.isnumeric():
                    last_digit = char
                    break
            
            calibration_value = first_digit + last_digit
            calibration_value_sum += int(calibration_value)

        print(calibration_value_sum)