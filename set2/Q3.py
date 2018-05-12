"""
Find the "continental divide" in a 2d height map

You are given a 2d rectangular array of positive integers representing the
height map of a continent. The "Pacific ocean" touches the left and top edges
of the array and the "Atlantic ocean" touches the right and bottom edges.

Find the "continental divide". That is, the list of grid points where water can
flow either to the Pacific or the Atlantic.
Water can only flow from a cell to another one with height equal or lower.

Example:

Pacific ~ ~ ~ ~ ~ |__
 ~ 1  2  2  3 (5) ~
 ~ 3  2  3 (4)(4) ~
 ~ 2  4 (5) 3  1 ~
 ~(6)(7) 1  4  5 ~
__(5) 1  1  2  4 ~
  |~ ~ ~ ~ ~ Atlantic

The answer would be the list containing the coordinates of all circled cells:
[(4,0), (3,1), (4,1), (2,2), (0,3), (1,3), (0,4)]
"""

import copy

NEIGHTBOURS = (
    (-1, 0),
    ( 1, 0),
    (0, -1),
    (0,  1)
)

def get_neighbours(pos, flow):

    h, w = len(flow), len(flow[0])

    valid_neigh = []
    for i, j in NEIGHTBOURS:
        next_pos = pos[0] + i, pos[1] + j
        if next_pos[0] < 0 or next_pos[0] >= h or \
           next_pos[1] < 0 or next_pos[1] >= w:
            continue

        if flow[next_pos[0]][next_pos[1]] == 0:
            valid_neigh.append((i, j))

    return valid_neigh


def calc_flow(pos, map2d, flow):
    flow[pos[0]][pos[1]] = 1

    cur_val = map2d[pos[0]][pos[1]]

    for neigh in get_neighbours(pos, flow):
        next_pos = pos[0] + neigh[0], pos[1] + neigh[1]

        if cur_val > map2d[next_pos[0]][next_pos[1]]:
            continue

        calc_flow(next_pos, map2d, flow)


def test_Q3():

    map2d = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]

    h, w = len(map2d), len(map2d[0])

    pacific_flow = [
        [0 for i in range(w)]
        for j in range(h)
    ]
    atlantic_flow = copy.deepcopy(pacific_flow)

    for i in range(w):
        calc_flow((0, i), map2d, pacific_flow)
    for i in range(1, h):
        calc_flow((i, 0), map2d, pacific_flow)

    for i in range(w):
        calc_flow((h-1, i), map2d, atlantic_flow)
    for i in range(0, h-1):
        calc_flow((i, w-1), map2d, atlantic_flow)

    for i in range(w):
        for j in range(h):
            if pacific_flow[j][i] == 1 and atlantic_flow[j][i] == 1:
                print((i, j))


if __name__ == "__main__":
    test_Q3()