def find_winner(boards_dict, winner_board):
    for key, board in boards_dict.items():
        # print(key)
        for row in board:
            # print("\t Row", row)
            winner = 0
            for drawn in row:
                # print("\t\t", drawn)
                if False not in drawn:
                    winner += 1
            if winner == 5:
                winner_board.append(board)
                return True

        for column in zip(*board):
            # print("\t Column", column)
            winner = 0
            for drawn in column:
                # print("\t\t", drawn)
                if False not in drawn:
                    winner += 1
            if winner == 5:
                winner_board.append(board)
                return True
    return False


def find_last_winner(boards_dict, last_winner):
    print(f"boards len - {len(boards_dict)}")
    # print(boards_dict)
    keys_to_pop = set()
    for key, board in boards_dict.items():
        # print(key)
        for row in board:
            # print("\t Row", row)
            winner = 0
            for drawn in row:
                # print("\t\t", drawn)
                if False not in drawn:
                    winner += 1
            if winner == 5:
                keys_to_pop.add(key)

        for column in zip(*board):
            # print("\t Column", column)
            winner = 0
            for drawn in column:
                # print("\t\t", drawn)
                if False not in drawn:
                    winner += 1
            if winner == 5:
                keys_to_pop.add(key)

    print(f"keys_to_pop {keys_to_pop}")
    for pop_key in keys_to_pop:
        if len(boards_dict) == 1:
            last_winner.append(list(boards_dict.values()))
        boards_dict.pop(pop_key)
        print(f"popped board {pop_key}")
    return True


with open("boards.txt") as boards:
    numbers = boards.readline().strip().split(",")
    _boards = []
    for board in boards:
        board = board.strip()
        if not board == "":
            board = board.split(" ")
            if not board == " ":
                _boards.append([(number, False) for number in board if not number == ""])

    boards_dict = {}
    board_number = 1
    board_numbers = []
    for i, _board in enumerate(_boards):
        i = i + 1
        board_numbers.append(_board)
        if i % 5 == 0:
            boards_dict[board_number] = list(board_numbers)
            board_number += 1
            board_numbers.clear()

    have_winner = False
    for number in numbers:
        print("\nNumber", number)
        for key, board in boards_dict.items():
            # print("\tNovi board", board)
            for row in board:
                for i, tuple_number in enumerate(row):
                    if number in tuple_number:
                        list_number = list(tuple_number)
                        list_number[1] = not list_number[1]
                        tuple_number = tuple(list_number)
                        row[i] = tuple_number
                # print("\t\trow", row)
        winner_board = []
        last_winner = []
        if not have_winner:
            winner = find_winner(boards_dict, winner_board)
            # winner = False
            if winner:
                final_sum = 0
                for row in winner_board[0]:
                    print(row)
                    for drawn in row:
                        print("\t", drawn)
                        if not drawn[1]:
                            final_sum += int(drawn[0])
                print(final_sum)
                print(number)
                print(int(number) * final_sum)
                boards_dict.pop(key)
                have_winner = True
        else:
            find_last_winner(boards_dict, last_winner)
            if last_winner:
                final_sum = 0
                for row in last_winner[0]:
                    print(row)
                    for drawn in row:
                        for element in drawn:
                            print("\t\t\t", element)
                            if not element[1]:
                                final_sum += int(element[0])
                        print("\t", drawn)
                print(final_sum)
                print(number)
                print(int(number) * final_sum)
                break
