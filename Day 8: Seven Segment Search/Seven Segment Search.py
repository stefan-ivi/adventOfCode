def among_unique(output_signal):
    if len(output_signal) == 2:
        return True
    elif len(output_signal) == 3:
        return True
    elif len(output_signal) == 4:
        return True
    elif len(output_signal) == 7:
        return True
    else:
        return False


with open("signals.txt") as signals:
    encodings = []
    for signal in signals:
        signal = signal.strip().split(" | ")
        signal = ([encodes.split(" ") for encodes in signal])
        encodings.append(signal)

    count_unique = 0
    for encoding in encodings:
        for output_signal in encoding[1]:
            if among_unique(output_signal):
                count_unique += 1
        len_six = []
        len_five = []
        for input_signal in encoding[0]:
            if len(input_signal) == 2:
                len_two = input_signal
            elif len(input_signal) == 3:
                len_three = input_signal
            elif len(input_signal) == 4:
                len_four = input_signal
            elif len(input_signal) == 5:
                len_five.append(input_signal)
            elif len(input_signal) == 6:
                len_six.append(input_signal)
            elif len(input_signal) == 7:
                len_seven = input_signal

        # print(f"len 7 {len_seven}")
        # print(f"len 6 {len_six}")
        # print(f"len 5 {len_five}")
        # print(f"len 4 {len_four}")
        # print(f"len 3 {len_three}")
        # print(f"len 2 {len_two}")

        #   ***
        #  |   |
        #  |   |
        #   ---
        #  |   |
        #  |   |
        #   ---
        for signal in len_three:
            if signal not in len_two:
                middle_top = signal

        #   ---
        #  |   |
        #  |   |
        #   ***
        #  |   |
        #  |   |
        #   ---
        same_len_five = [signal for signal in len_five[0] if signal in len_five[1]]
        same_len_five.remove(f"{middle_top}")
        middle_middle = [signal for signal in same_len_five if signal in len_four][0]

        #   ---
        #  |   |
        #  |   |
        #   ---
        #  |   |
        #  |   |
        #   ***
        same_len_five.remove(f"{middle_middle}")
        middle_bottom = same_len_five[0]

        #   ---
        #  *   |
        #  *   |
        #   ---
        #  |   |
        #  |   |
        #   ---
        for signal in len_four:
            if signal is not middle_middle and signal not in len_two:
                left_top = signal

        #   ---
        #  |   |
        #  |   |
        #   ---
        #  |   *
        #  |   *
        #   ---
        for signal in len_five:
            if left_top in signal:
                for sign in signal:
                    if sign is not middle_middle and sign is not middle_bottom and sign is not middle_top and sign is not left_top:
                        right_bottom = sign

        #   ---
        #  |   *
        #  |   *
        #   ---
        #  |   |
        #  |   |
        #   ---
        for signal in len_two:
            if signal is not right_bottom:
                right_top = signal

        #   ---
        #  |   |
        #  |   |
        #   ---
        #  *   |
        #  *   |
        #   ---
        for signal in len_five:
            for encoding in signal:
                if encoding is not middle_middle and encoding is not middle_top and encoding is not middle_bottom and encoding is not right_top and encoding is not left_top and encoding is not right_bottom:
                    left_bottom = encoding

    final_sum = 0
    for signals in encodings:
        output = ''
        for signal in signals[1]:
            if len(signal) == 2:
                output += '1'
            elif len(signal) == 3:
                output += '7'
            elif len(signal) == 4:
                output += '4'
            elif len(signal) == 7:
                output += '8'
            elif len(signal) == 5:
                if middle_top in signal and right_top in signal and middle_middle in signal and left_bottom in signal and middle_bottom in signal:
                    output += "2"
                if middle_top in signal and right_top in signal and middle_middle in signal and right_bottom in signal and middle_bottom in signal:
                    output += "3"
                if middle_top in signal and left_top in signal and middle_middle in signal and right_bottom in signal and middle_bottom in signal:
                    output += "5"
            else:
                if middle_top in signal and right_top in signal and left_top in signal and right_bottom in signal and left_bottom in signal and middle_bottom in signal:
                    output += "0"
                if middle_top in signal and middle_middle in signal and left_top in signal and right_bottom in signal and left_bottom in signal and middle_bottom in signal:
                    output += "6"
                if middle_top in signal and right_top in signal and left_top in signal and right_bottom in signal and middle_middle in signal and middle_bottom in signal:
                    output += "9"
        print(output)

        final_sum += int(output)

    print(f"part one = {count_unique}")
    print(f"part two = {final_sum}")
