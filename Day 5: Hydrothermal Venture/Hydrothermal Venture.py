def make_coords(lines):
    lines = "".join(lines)
    lines = lines.split(" -> ")
    lines = [line.split(",") for line in lines]
    lines = [tuple(int(number) for number in line) for line in lines]

    return lines


def fill_the_dict(coord_list, dict_positions):
    if type(coord_list[0]) == list:
        match = coord_list[1]
        for coord in coord_list[0]:
            if (coord, match) in dict_positions:
                dict_positions[(coord, match)] += 1
            else:
                dict_positions[(coord, match)] = 1
    else:
        for coord in coord_list[1]:
            match = coord_list[0]
            if (match, coord) in dict_positions:
                dict_positions[(match, coord)] += 1
            else:
                dict_positions[(match, coord)] = 1

    # print(f"dict - {dict_positions}")


# def create_matrix(coord_list):
#     if type(coord_list[0]) == list:
#         # for
#
#     print(coord_list)


def matched_line(coords, match, dict_positions):
    coord = coords[0]
    coord1 = coords[1]
    print(f"coord - {coord}")
    print(f"coord1 - {coord1}")

    if not coord[0] == match:
        if coord[0] < coord1[0]:
            coord_list = (list(range(coord[0], coord1[0] + 1)), match)
        else:
            coord_list = (list(range(coord[0], coord1[0] - 1, -1)), match)
    else:
        if coord[1] < coord1[1]:
            coord_list = (match, list(range(coord[1], coord1[1] + 1)))
        else:
            coord_list = (match, list(range(coord[1], coord1[1] - 1, -1)))
    print(f"tuple - {coord_list}")
    fill_the_dict(coord_list, dict_positions)
    # create_matrix(coord_list)
    print()


with open("coordinates.txt") as coordinates:
    coordinates = [make_coords(line.strip()) for line in coordinates]
    horizontal_line = []
    vertical_line = []
    matched_position = {}
    for coords in coordinates:
        # for coord in coords:
        # print(coord)
        # print()
        for zip_coord in zip(*coords):
            # print(f"zip* {zip_coord}")
            if zip_coord[0] == zip_coord[1]:
                # print(f"match zip* {zip_coord[0]}, {coords}")
                matched_line(coords, zip_coord[0], matched_position)

    count_overlaps = 0
    print(len(matched_position))
    for value in matched_position.values():
        if value > 1:
            count_overlaps += 1
        # if value == 2:
        #     # print(value)
        #     count_overlaps += 1
        # if value == 3:
        #     # print(value)
        #     count_overlaps += 2
        # if value == 4:
        #     # print(value)
        #     count_overlaps += 3
        # if value == 5:
        #     # print(value)
        #     count_overlaps += 4
    #     6130 too high
    #     5956 too low
    # for key, value in matched_position.items():
    #     print(key, value)

    # print(len(matched_position))
    print(count_overlaps)
