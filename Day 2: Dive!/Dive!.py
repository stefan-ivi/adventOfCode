def part_one():
    with open("commands.txt") as commands:
        curr_depth = 0
        horizontal_position = 0
        for command in commands:
            command = command.strip().split(" ")
            if command[0].startswith("forward"):
                horizontal_position = horizontal_position + int(command[1])
            elif command[0].startswith("down"):
                curr_depth = curr_depth + int(command[1])
            else:
                curr_depth = curr_depth - int(command[1])
        print(curr_depth)
        print(horizontal_position)
        print(curr_depth * horizontal_position)


def part_two():
    curr_depth = 0
    horizontal_position = 0
    aim = 0
    with open("commands.txt") as commands:
        for command in commands:
            command = command.strip().split(" ")
            if command[0].startswith("forward"):
                horizontal_position = horizontal_position + int(command[1])
                curr_depth = curr_depth + int(command[1]) * aim
            elif command[0].startswith("down"):
                aim = aim + int(command[1])
            else:
                aim = aim - int(command[1])
        print(curr_depth)
        print(horizontal_position)
        print(aim)
        print(curr_depth * horizontal_position)


part_two()
