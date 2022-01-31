def increase(depth, curr_depth):
    return depth > curr_depth if 1 else 0


def part_one():
    num_of_increases = 0
    with open('depth.txt') as all_depths:
        curr_depth = 0
        for depth in all_depths:
            depth = int(depth.strip())
            num_of_increases = num_of_increases + increase(depth, curr_depth)
            curr_depth = depth
    return num_of_increases - 1


def part_two():
    list_depth = []
    with open('depth.txt') as all_depths:
        for depth in all_depths:
            list_depth.append(int(depth.strip()))

    num_of_increases = 0
    curr_depth = 0
    for depth1, depth2, depth3 in zip(list_depth, list_depth[1:], list_depth[2:]):
        depth = depth1 + depth2 + depth3
        num_of_increases = num_of_increases + increase(depth, curr_depth)
        curr_depth = depth

    return num_of_increases - 1


print(part_one())
print(part_two())
