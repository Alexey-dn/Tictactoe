def intro():
    print("Hi, dude.")
    print("It's a prototype of a new breathtaking game.")
    print("That's named Tic-Tac-Toe.")
    print("You should enter coordinates x and y.")
    print("Where x and y are a row and a column number correspondingly.")
    print("Let's roll.")


intro()
field = [[" ", " ", " "] for _ in range(3)]


def disp_output():
    print("Y\X 0   1   2")
    print(f"0   {field[0][0]} | {field[0][1]} | {field[0][2]}")
    print("  --------------")
    print(f"1   {field[1][0]} | {field[1][1]} | {field[1][2]}")
    print("  --------------")
    print(f"2   {field[2][0]} | {field[2][1]} | {field[2][2]}")


def ask_and_check():
    while True:
        tmp = input("Your turn. Enter coordinates:\t").split()
        if len(tmp) != 2:
            print("Your coordinates have to consist of one digit for x and for y as well."
                  "Enter them once again.")
            continue

        if not (tmp[0].isdigit() and tmp[1].isdigit()):
            print("Your coordinates have to be digits. Enter them once again.")
            continue

        x, y = map(int, tmp)

        if not (0 <= x <= 2 or 0 <= y <= 2):
            print("Your coordinates are out of range. Enter them once again.")
            continue

        if field[x][y] != " ":
            print("This cell isn't empty. Choose another coordinates.")
            continue
        return x, y


def win():
    win_res = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in win_res:
        result = []
        for a in i:
            result.append(field[a[0]][a[1]])
        if result == ["X", "X", "X"]:
            print("X won!")
            return True
        if result == ["0", "0", "0"]:
            print("0 won!")
            return True
    return False


cnt = 0
while True:
    cnt += 1
    disp_output()

    if cnt % 2 == 1:
        print("0 turns")
    else:
        print("X turns")

    x, y = ask_and_check()

    if cnt % 2 == 1:
        field[x][y] = "0"
    else:
        field[x][y] = "X"

    if win():
        break

    if cnt == 9:
        print("Nobody won")
        break
