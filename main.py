print("Let's Play Tic-Tac-Toe Together :) \n")
print("Note:- To mark the desired position in a 3X3 board, you gave to give a number as input.\n"
      "for example 12(here 1 digit is the number determining row and the second digit is the column number.\n")


def add_value(digit, char):
    if digit[0] == '1':
        value_holding_list[int(digit[1])-1] = char
    elif digit[0] == '2':
        value_holding_list[int(digit[1])+2] = char
    else:
        value_holding_list[int(digit[1])+5] = char


def is_finished():
    for i in range(0, 7, 3):
        if value_holding_list[i] == value_holding_list[i+1] == value_holding_list[i+2] != "   ":
            return value_holding_list[i]
    for i in range(3):
        if value_holding_list[i] == value_holding_list[i+3] == value_holding_list[i+6] != "   ":
            return value_holding_list[i]
    if value_holding_list[0] == value_holding_list[4] == value_holding_list[8] != "   ":
        return value_holding_list[0]
    elif value_holding_list[2] == value_holding_list[4] == value_holding_list[6] != "   ":
        return value_holding_list[2]
    return False


def play_game():

    char = " O "
    used_places = []
    while '   ' in value_holding_list:
        winner_char = is_finished()

        if winner_char:
            print(f"Bingo player{winner_char} won the game!")
            break

        print(f"Player {char} ")
        marking_digit = input("Where do you want to mark? :- ")
        if marking_digit in used_places:
            continue
        elif marking_digit in ['11', '12', '13', '21', '22', '23', '31', '32', '33']:
            used_places.append(marking_digit)
            add_value(marking_digit, char=char)
            board = f"""
            _____________
            |{value_holding_list[0]}|{value_holding_list[1]}|{value_holding_list[2]}|
            |-----------|
            |{value_holding_list[3]}|{value_holding_list[4]}|{value_holding_list[5]}|
            |-----------|
            |{value_holding_list[6]}|{value_holding_list[7]}|{value_holding_list[8]}|
            |-----------|
            """
            print(board)
        else:
            print("Invalid input")
            continue
        char = " X " if char == " O " else " O "


value_holding_list = ['   ', ]*9

play_game()
while input("Do you want to play again, type 'Yes' or 'No': ").lower() == 'yes':
    value_holding_list = ['   ', ]*9
    play_game()
