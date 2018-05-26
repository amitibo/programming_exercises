"""Find the minimum weight path on a triangle.
"""



def find_minimum_weight(triangle):

    weights = triangle[0]

    for d, row in enumerate(triangle[1:]):
        new_weights = []

        for i, val in enumerate(row):
            if i == 0:
                min_path = weights[0]
            elif i == d+1:
                min_path = weights[-1]
            else:
                min_path = min(weights[i-1], weights[i])

            new_weights.append(min_path + val)

        weights = new_weights

    return min(weights)


def main():

    tests = (
        (
            (
                (2,),
                (4, 4),
                (8, 5, 6),
                (4, 2, 4, 2),
                (1, 5, 2, 3, 4)
            ),
            15
        ),
    )

    for triangle, w in tests:
        ans = find_minimum_weight(triangle)
        assert  ans == w, f"Wrong weight: {ans} != {w}"


if __name__ == "__main__":
    main()