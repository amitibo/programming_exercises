"""Find a path in the maze (DFS)."""

import collections


BLACK, WHITE = range(2)


def find_path(maze : list, src : tuple, dst : tuple):

    def find_path_helper(curr : tuple, path=[], visited=set()):

        if curr == dst:
            return path

        visited.add(curr)

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            next = curr[0] + dy, curr[1] + dx

            if next[0] < 0 or next[0] >= len(maze) or \
               next[1] < 0 or next[1] >= len(maze[0]) or \
               maze[next] == BLACK or next in visited:
                continue

            res = find_path_helper(next, path + [next], visited)

            if res:
                return res

        return []

    return find_path(src)
