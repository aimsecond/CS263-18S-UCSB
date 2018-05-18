# The Computer Language Benchmarks Game
# http://benchmarksgame.alioth.debian.org/
#
# contributed by Olof Kraigher
# modified by Tupteq
# 2to3

from __future__ import print_function
import sys

width = 5
height = 10

rotate = dict(E='NE', NE='NW', NW='W', W='SW', SW='SE', SE='E')
flip = dict(E='W', NE='NW', NW='NE', W='E', SW='SE', SE='SW')
move = dict(E=lambda x, y: (x+1, y),
            W=lambda x, y: (x-1, y),
            NE=lambda x, y: (x + (y%2), y-1),
            NW=lambda x, y: (x + (y%2) - 1, y-1),
            SE=lambda x, y: (x + (y%2), y+1),
            SW=lambda x, y: (x + (y%2) - 1, y+1))

solutions = []
masks = 10 * [0]

valid = lambda x, y: 0 <= x < width and 0 <= y < height
zerocount = lambda mask: sum([(1<= 0):
            if (masks[j] & cellMask) == cellMask:
                masksAtCell[cellCounter][color].append(masks[j])
                j = j-1
            else:
                cellMask = cellMask >> 1
                cellCounter -= 1
        color += 1


def solveCell(cell, board):
    if to_go <= 0:
        # Got enough solutions
        pass
    elif board == 0x3FFFFFFFFFFFF:
        # Solved
        addSolutions()
    elif board & (1 << cell) != 0:
        # Cell full
        solveCell(cell-1, board)
    elif cell < 0:
        # Out of board
        pass
    else:
        for color in range(10):
            if masks[color] == 0:
                for mask in masksAtCell[cell][color]:
                    if mask & board == 0:
                        masks[color] = mask
                        solveCell(cell-1, board | mask)
                        masks[color] = 0


def addSolutions():
    global to_go
    s = ''
    mask = 1
    for y in range(height):
        for x in range(width):
            for color in range(10):
                if masks[color] & mask != 0:
                    s += str(color)
                    break
                elif color == 9:
                    s += '.'
            mask <<= 1

    # Inverse
    ns = ''
    for y in range(height):
        for x in range(width):
            ns += s[width - x - 1 + (width - y - 1) * width]

    # Finally append
    solutions.append(s)
    solutions.append(ns)
    to_go -= 2


def printSolution(solution):
    for y in range(height):
        for x in range(width):
            print(solution[x + y*width], end=' ')

        print("")
        if y % 2 == 0:
            print("", end=' ')
    print()


def solve(n):
    global to_go
    to_go = n
    generateBitmasks()
    solveCell(width*height - 1, 0)


if __name__ == "__main__":
    solve(int(sys.argv[1]))

    print("%d solutions found\n" % len(solutions))
    printSolution(min(solutions))
    printSolution(max(solutions))