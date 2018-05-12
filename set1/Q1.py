"""
Q1
--
Given a postfix statements such as (((5 2 -7 +) 8 1 *)5 -2 *) meaning
(((5+2+(-7))*8*1)*(5*(-2))), Write an algorithm which gets a postfix
expression as input and returns the result.
"""

import functools

operator_map = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '-': lambda x, y: x - y,
}


def tokenize(chars):
    """Convert a string of characters into a list of tokens."""

    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def calculate_expression(exp):
    """Calculate an expression of type: [X0, X1, ..., <OPERATOR>]"""

    if len(exp) == 0:
        return 0

    assert exp[-1] in operator_map, "Unkown operator: {}".format(exp[-1])

    return functools.reduce(operator_map[exp[-1]], exp[:-1])


def read_from_tokens(tokens):
    """Read an expression from a list of tokens"""

    assert len(tokens) > 0, "Unexpected EOF."

    val = 0
    exp = []
    while len(tokens) > 0:
        n = tokens.pop(0)

        if n == "(":
            val, tokens = read_from_tokens(tokens)
            exp.append(val)
        elif n == ")":
            return calculate_expression(exp), tokens
        else:
            try:
                exp.append(int(n))
            except:
                try:
                    exp.append(float(n))
                except:
                    exp.append(n)

    return val, []


def parse(statement):
    """Evaluate a statement."""

    return read_from_tokens(tokenize(statement))[0]


def test_Q1():

    tests = (
        ("()", 0),
        ("(((5 2 -7 +) 8 1 *)5 -2 *)", 0),
        ("(((5 3 -7 +) 8 1 *)5 -2 *)", -80),
    )

    for stat, answer in tests:
        calculation = parse(stat)
        assert calculation == answer, \
               "Q1 error. Expected {}, but got {}".format(
                   answer, calculation
               )


if __name__ == "__main__":
    test_Q1()