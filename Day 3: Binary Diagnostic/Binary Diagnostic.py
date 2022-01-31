def count(values):
    zeroo = 0
    ones = 0
    for value in values:
        if int(value) == 0:
            zeroo += 1
        else:
            ones += 1
    return zeroo, ones


def part_one():
    with open("diagnostics.txt") as diagnostics:
        binary_dict = {}
        for diagnostic in diagnostics:
            diagnostic = diagnostic.strip()
            for i in range(len(diagnostic)):
                if i in binary_dict:
                    binary_dict[i].append(diagnostic[i])
                else:
                    binary_dict[i] = [diagnostic[i]]

    gamma = ""
    epsilon = ""

    for values in binary_dict.values():
        zeros, ones = count(values)
        if zeros > ones:
            gamma += str(0)
            epsilon += str(1)
        else:
            gamma += str(1)
            epsilon += str(0)
    print(int(gamma, 2), gamma)
    print(int(epsilon, 2), epsilon)
    print(int(gamma, 2) * int(epsilon, 2))


def part_one_v2():
    with open("diagnostics.txt") as diagnostics:
        inverse_diagnostics = [star_diagnostic for star_diagnostic in zip(*diagnostics)]

    gamma = ""
    epsilon = ""
    for inverse_diagnostic in inverse_diagnostics:
        zeros, ones = count(inverse_diagnostic)
        if zeros > ones:
            gamma += str(0)
            epsilon += str(1)
        else:
            gamma += str(1)
            epsilon += str(0)
    print(int(gamma, 2) * int(epsilon, 2))


def find_larger(diagnostics, i):
    if len(diagnostics) == 1:
        return diagnostics

    bits_ones = []
    bits_zeros = []

    for diagnostic in diagnostics:
        if int(diagnostic[i]) == 1:
            bits_ones.append(diagnostic)
        else:
            bits_zeros.append(diagnostic)
    print(diagnostics)

    if len(bits_ones) >= len(bits_zeros):
        i += 1
        return find_larger(bits_ones, i)
    else:
        i += 1
        return find_larger(bits_zeros, i)


def find_smaller(diagnostics, i):
    if len(diagnostics) == 1:
        return diagnostics

    bits_ones = []
    bits_zeros = []

    for diagnostic in diagnostics:
        if int(diagnostic[i]) == 1:
            bits_ones.append(diagnostic)
        else:
            bits_zeros.append(diagnostic)

    if len(bits_ones) < len(bits_zeros):
        i += 1
        return find_smaller(bits_ones, i)
    else:
        i += 1
        return find_smaller(bits_zeros, i)


def part_two():
    with open("diagnostics.txt") as diagnostics:
        i = 0
        diagnostics = [diagnostic.strip() for diagnostic in diagnostics]

        oxygen = find_larger(diagnostics, i)
        print(oxygen, int(oxygen[0], 2))

        co2 = find_smaller(diagnostics, i)
        print(co2, int(co2[0], 2))

        print(int(oxygen[0], 2) * int(co2[0], 2))


# part_one()
# part_one_v2()
part_two()
