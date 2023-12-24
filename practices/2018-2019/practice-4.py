class Dot:

    def __init__(self, color, updatable=True, value=None):
        self.color = color
        self.updatable = updatable
        self.value = value

    def __str__(self):
        str_value = " "

        if self.color == "R":
            str_value = "R"
        elif self.color == "B":
            str_value = str(self.value) if self.value > 0 else "B"


        return "[{}]".format(str_value)


class Board:
    def __init__(self, filename):
        self.board = Board.fromFile(filename)
        self.filename = filename
        self.cols = len(self.board[0])
        self.rows = len(self.board)

    @staticmethod
    def fromFile(filename):
        with open(filename, "r") as fd:
            csv_data = csv.reader(fd)


            board = []
            for row in csv_data:
                board_row = []
                for item in row:
                    if item == ".":
                        dot = Dot("R", updatable=False)
                    elif item == "*":
                        dot = Dot("B", updatable=False, value=0)
                    elif item.isdigit():
                        dot = Dot("B", updatable=False, value=int(item))
                    else:
                        dot = Dot("G")

                    board_row.append(dot)

                board.append(board_row)

        return board

    def addDot(self, x, y, color):
        if not self.inbounds(x, y):
            print("ERROR: Coordinates ({},{}) are out of bounds".format(x, y))
            return

        dot = self.board[y][x]

        if not dot.updatable:
            print("ERROR: Dot ({},{}) is not updatable".format(x, y))
            return

        dot_value = 0 if color == "B" else None
        self.board[y][x] = Dot(color, value=dot_value)

    def removeDot(self, x, y):
        if not self.inbounds(x, y):
            print("ERROR: Coordinates ({},{}) are out of bounds".format(x, y))
            return

        dot = self.board[y][x]

        if not dot.updatable:
            print("ERROR: Dot ({},{}) is not updatable".format(x, y))
            return

        self.board[y][x] = Dot("G")

    def isCompleted(self):
        for x in range(0, self.cols):
            for y in range(0, self.rows):
                dot = self.board[y][x]
                if dot.color == "B" and dot.value > 0:
                    blue_neighbors = self.countNeighbors(x, y, "B")
                    if blue_neighbors != dot.value:
                        print("Completed=False. Expected {} blue neighbors for dot at ({},{}) but {} found".format(dot.value, x, y, blue_neighbors))
                        return False
                elif dot.color == "G":
                    print("Completed=False. Found a grey dot at {},{}".format(x, y))
                    return False

        print("Completed=True")
        return True

    def isCompletable(self):
        for x in range(0, self.cols):
            for y in range(0, self.rows):
                dot = self.board[y][x]
                if dot.color == "B" and dot.value > 0:
                    blue_neighbors = self.countNeighbors(x, y, "B")
                    print("{},{}: Seen blue neighbors {}, expected {}".format(x, y, blue_neighbors, dot.value))
                    if blue_neighbors > dot.value:
                        print("Completable=False. The dot ({}, {}) sees too many blue dots".format(x, y))
                        return False
                    blue_neighbors = self.countNeighbors(x, y, "B", strict=False)
                    grey_neighbors = self.countNeighbors(x, y, "G", strict=False)
                    if (blue_neighbors + grey_neighbors) < dot.value:
                        print("Completable=False. There is not enough spots for the dot ({},{}) to see {} blue dots".format(x, y, dot.value))
                        return False

        print("Completable=True")
        return True

    def inbounds(self, x, y):

        return x < self.cols and y < self.rows

    def countNeighbors(self, x, y, color, strict=True):

        if not self.inbounds(x, y):
            print("ERROR: Coordinates out of bounds")
            return

        count = 0

        crd = x + 1
        while crd < self.cols:
            dot = self.board[y][crd]
            if dot.color == color:
                count += 1
            elif strict or dot.color == "R":
                break
            crd += 1

        crd = x - 1
        while crd >= 0:
            dot = self.board[y][crd]
            if dot.color == color:
                count += 1
            elif strict or dot.color == "R":
                break
            crd -= 1

        crd = y - 1
        while crd >= 0:
            dot = self.board[crd][x]
            if dot.color == color:
                count += 1
            elif strict or dot.color == "R":
                break
            crd -= 1

        crd = y + 1
        while crd < self.rows:
            dot = self.board[crd][x]
            if dot.color == color:
                count += 1
            elif strict or dot.color == "R":
                break
            crd += 1

        return count

    def __str__(self):
        lines = []
        for row in self.board:
            lines.append("".join([str(item) for item in row]))

        return "\n".join(lines)


def playgame(filename):
    board = Board(filename)
    doExit = False

    while not doExit and not board.isCompleted():
        print(board)

        userInput = input("Your input: ")


        if userInput.startswith("exit"):
            doExit = True
            break
        elif userInput.startswith("add"):
            command = [x.strip() for x in userInput.split(",")]
            if len(command) == 4:
                board.addDot(int(command[1]), int(command[2]), command[3])
            else:
                print("ERROR: Invalid format")


        if not board.isCompletable():
            print("The board is not completable, try removing some dots")

    if doExit:
        print("Bye!")
    elif board.isCompleted():
        print("The board is completed, congratulations!")


if __name__ == "__main__":
    print("Mostrar tablero")
    board = Board("res/5x5.txt")
    print(board)

    print("Añadir punto azul en (1,0)")
    board.addDot(1, 0, "B")
    print(board)

    print("Eliminar punto en (1,0)")
    board.addDot(1, 0, "G")
    print(board)

    print("Añadir punto rojo en (1,0)")
    board.addDot(1, 0, "R")
    print(board)

    print("Eliminar punto en (1,0)")
    board.removeDot(1, 0)
    print(board)

    print("Comprobar si el tablero esta completo")
    print(board)
    board.countNeighbors(0, 0, "B")
    print("Board completed = " + str(board.isCompleted()))

    print("Comprobar si el tablero esta completo")
    board2 = Board("res/4x4_completed.txt")
    print(board2)
    print("Board completed = " + str(board2.isCompleted()))

    print("Comprobar si el tablero es completable")
    board3 = Board("res/4x4_not_completable.txt")
    print(board3)
    print("Board completable = " + str(board3.isCompletable()))

    print("Jugar al juego")
    playgame("res/4x4_playgame.txt")
