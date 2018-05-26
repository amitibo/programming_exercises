"""The gasup problem.
"""

import numpy as np

DPG = 20


def gasup(distances, gas, dpg=DPG):
    gas *= dpg
    sums = np.cumsum(gas - distances)

    return (np.argmin(sums) + 1) % len(gas)


def main():
    distances = np.array((200, 400, 600, 200, 100, 900, 600))
    gas = np.array((5, 30, 25, 10, 10, 50, 20))

    print("Found the ample city: {}".format(gasup(distances, gas)))


if __name__ == "__main__":
    main()