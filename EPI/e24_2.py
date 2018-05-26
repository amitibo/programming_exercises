"""Find First Missing POSITIVE ENTRY
"""


def find_missing_on(A):
    B = [0] * len(A)

    for i, a in enumerate(A):
        if a > 0:
            B[a] = a

    for i, b in enumerate(B[1:]):
        if b < 1:
            return i+1


def find_missing(A):

    n = len(A)
    for i in range(n):
        if 1 <= A[i] <= n:
            A[A[i]-1], A[i] = A[i], A[A[i]-1]

    print(A)

    for i in range(n):
        if A[i] != i+1:
            return i+1


def main():

    A = [3, 5, 4, -1, 5, 1, -1]
    print(find_missing(A))


if __name__ == "__main__":
    main()