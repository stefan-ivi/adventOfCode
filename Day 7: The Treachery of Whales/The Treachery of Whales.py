import math


def compute_cost(horizontal_positions, mid):
    cost = 0
    for i, horizontal_position in enumerate(horizontal_positions):
        print(f"\thorizontal_position {horizontal_position} - mid {mid}")
        cost += abs(horizontal_position - mid)
    return cost


def min_cost(horizontal_positions):
    min_position = min(horizontal_positions)
    max_position = max(horizontal_positions)

    while (max_position - min_position) > 2:
        print()
        print(f"min_position {min_position}")
        print(f"max_position {max_position}")

        min_mid = min_position + (max_position - min_position) // 3
        max_mid = max_position - (max_position - min_position) // 3

        print(f"min_mid {min_mid}")
        print(f"max_mid {max_mid}")

        cost1 = compute_cost(horizontal_positions, min_mid)
        print(f"cost1 {cost1}")
        cost2 = compute_cost(horizontal_positions, max_mid)
        print(f"cost2 {cost2}")

        if cost1 < cost2:
            max_position = max_mid
        else:
            min_position = min_mid

    return compute_cost(horizontal_positions, (min_position + max_position) // 2)


def find_cost(horizontal_positions):
    min_position = min(horizontal_positions)
    max_position = max(horizontal_positions)
    least_cost = math.inf


with open("horizontal_positions.txt") as horizontal_positions:
    horizontal_positions = horizontal_positions.readline().split(",")
    horizontal_positions = [int(horizontal_position) for horizontal_position in horizontal_positions]
    # print(min_cost(horizontal_positions))

    find_cost(horizontal_positions)
