import random
import time
import os

h = 20
w = 20

alive = "0"
dead = "."


def createBoard():
    board = []
    for _ in range(h):
        row = [random.choice([alive, dead]) for _ in range(w)]
        board.append(row)
    return board


def printBoard(board):
    for row in board:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)


def countAliveNeighbour(board, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[nx][ny] == alive:
                count += 1
    return count


def generateNew(board):
    new_board = []
    for x in range(len(board)):
        new_row = []
        for y in range(len(board[0])):
            alive_neighbours = countAliveNeighbour(board, x, y)
            cell = board[x][y]

            if cell == alive:
                if alive_neighbours in [2, 3]:
                    new_row.append(alive)
                else:
                    new_row.append(dead)
            else:
                if alive_neighbours == 3:
                    new_row.append(alive)
                else:
                    new_row.append(dead)
        new_board.append(new_row)
    return new_board


if __name__ == "__main__":
    board = createBoard()
    for _ in range(10):
        print(f"Generations {_+1}:")
        printBoard(board)
        board = generateNew(board)
        time.sleep(1)
        os.system("cls")
