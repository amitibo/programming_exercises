"""
Q2
--
Consider the following game: there is a board that looks like ___R__L__L where
a _ is an empty space and L and R are soldiers that can move only Left or
Right correspondingly. There can be no skipping, meaning that if two soldiers
are in the following state RL they can't move.
The question is: given a board with N tiles and some players on, design an
algorithm to verify if a future state is possible. For example:   ___R____LL
is not possible but  ____RL___L is possible.
"""

def check_char(c, i, list_R, list_L):
    if c == 'R':
        list_R.append(i)
    elif c == 'L':
        list_L.append(i)
    elif c != '_':
        raise ValueError("Unkown char {}".format(c))


def verify(start_state, end_state):

    assert len(start_state) == len(end_state), "Start and end boards differ in length"

    #
    # Verify that the order number of soldiers is possible
    # (ignoring movement direction)
    #
    if start_state.replace("_", "") != end_state.replace("_", ""):
        return False

    start_R, start_L = [], []
    end_R, end_L = [], []

    for i, (c0, c1) in enumerate(zip(start_state, end_state)):
        check_char(c0, i, start_R, start_L)
        check_char(c1, i, end_R, end_L)

    #
    # Verify that the order of soldiers is possible taking
    # in consideration the movement direction.
    #
    for i, j in zip(start_R + end_L, end_R + start_L):
        if i > j:
            return False

    return True


def test_Q2():

    tests = (
        ("___R__L__L", "___R____LL", False),
        ("___R__L__L", "____RL___L", True),
        ("___R__R__L", "___R____LL", False),
    )

    for start_state, end_state, answer in tests:

        calculation = verify(start_state, end_state)

        assert calculation == answer, \
               "Q2 error. Expected {}, but got {}".format(
                   answer, calculation
               )


if __name__ == "__main__":
    test_Q2()