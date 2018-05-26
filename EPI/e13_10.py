"""Team photo day 1.
"""

import collections
import copy
import random
import string
from tqdm import trange


def verify_photo(team0, team1):
    """Check if there is a "Producer sequence" connecting s to t."""

    assert len(team0) == len(team1), "Team lengths should match."

    team0 = sorted(team0)
    team1 = sorted(team1)

    if team1[-1] > team0[-1]:
        temp = team1
        team1 = team0
        team0 = temp

    i0, i1 = [0] * 2
    while i1 < len(team1):
        if team0[i0] > team1[i1]:
            i1 += 1
        elif team1[i1] > team0[i0]:
            i0 += 1
        else:
            i0 += 1
            i1 += 1

        if i1 < i0:
            return False

    return True



class Team():
    Player = collections.namedtuple("player", ('height'))

    def __init__(self, heights):
        self._players = [Team.Player(h) for h in heights]

    @staticmethod
    def valid_placement_exists(team0, team1):
        return all(
            a < b for a, b in zip(sorted(team0._players), sorted(team1._players))
        )


def main():

    N = 20

    team0 = [random.randint(0, 50) for _ in range(N)]
    team1 = [random.randint(0, 50) for _ in range(N)]

    print(sorted(team0))
    print(sorted(team1))
    print(verify_photo(team0, team1))
    print(
        Team.valid_placement_exists(Team(team0), Team(team1)) or \
        Team.valid_placement_exists(Team(team1), Team(team0))
    )

if __name__ == "__main__":
    main()