"""Towers of Hanoi
"""

N = 6

def compute_tower_hanoi(n):

    def hanoi_helper(n, src, dst):
        if n == 0:
            return []

        #
        # Find the helper peg
        #
        helper = list(range(3))
        helper.remove(src)
        helper.remove(dst)
        helper = helper[0]

        moves = hanoi_helper(n-1, src, helper)
        moves.append((src, dst))
        moves.extend(hanoi_helper(n-1, helper, dst))

        return moves

    return hanoi_helper(n, 0, 1)


def main():
    moves = compute_tower_hanoi(N)
    for m in moves:
        print(m)


if __name__ == "__main__":
    main()
