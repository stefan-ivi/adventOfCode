def new_lanternfish_part_1(ages):
    _ages = list(ages)
    for i in range(len((_ages))):
        if _ages[i] == 0:
            ages.append(8)
            ages[i] = 6
            continue
        ages[i] -= 1


def new_lanternfish_part_2(dict_ages):
    list_ages = list(age for age in dict_ages.values())
    print(f"dict {dict_ages}")
    print(f"list {list_ages}")
    # list_ages[-1] += 1
    dict_ages[0] = list_ages[1]
    dict_ages[1] = list_ages[2]
    dict_ages[2] = list_ages[3]
    dict_ages[3] = list_ages[4]
    dict_ages[4] = list_ages[5]
    dict_ages[5] = list_ages[6]
    dict_ages[6] = list_ages[7]
    dict_ages[7] = list_ages[8]
    dict_ages[8] = list_ages[0]
    dict_ages[6] += list_ages[0]
    print()


with open("ages.txt") as ages:
    ages = [int(age) for age in ages.readline().split(",")]

    dict_ages = {}
    for i in range(9):
        dict_ages[i] = 0
    for age in ages:
        if age in dict_ages.keys():
            dict_ages[age] += 1

    day = 1
    while day <= 256:
        # new_lanternfish_part_1(ages)
        new_lanternfish_part_2(dict_ages)
        list_ages = [age for age in dict_ages.values()]
        print(f"After day {day}: \t {sum(list_ages)}")
        day += 1

    # print(len(ages))
    # print(ages)

    print(sum(list_ages))
