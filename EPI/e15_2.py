"""Place n queens on NxN table.
"""

from collections import namedtuple


def place_queens(n):

    solutions = []
    columns_placement = []

    def queens_helper(row):
        if row == n:
            solutions.append(columns_placement[:])
            return

        for i in range(n):
            #
            # Verify
            #
            bad_placements = columns_placement[:]
            bad_placements.extend([(c + row - j) for  j, c in enumerate(columns_placement)])
            bad_placements.extend([(c - row + j) for  j, c in enumerate(columns_placement)])
            if i in bad_placements:
                continue

            columns_placement.append(i)
            queens_helper(row+1)
            columns_placement.pop(-1)

    queens_helper(0)
    return solutions


def place_queens_alternative(n):

    def queens_helper(row):
        if row == n:
            solutions.append(columns_placement)
            return

        for col in range(n):
            if all(
                abs(col-c) not in (0, row-i)
                for i, c in enumerate(columns_placement[:row])):
                columns_placement[row] = col
                queens_helper(row+1)

    solutions = []
    columns_placement = [0] * n

    queens_helper(0)

    return solutions


def main():
    #for solution in place_queens(4):
    #    print(solution)
    for solution in place_queens_alternative(4):
        print(solution)


if __name__ == "__main__":
    main()
