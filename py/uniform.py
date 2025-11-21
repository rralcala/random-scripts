from math import floor, log10
import sys


def getUniformIntegerCountInIntervalB(A: int, B: int) -> int:
    # Write your code here
    ans = 0
    a = len(str(A))
    b = len(str(B))
    while b >= a:
        for j in range(1, 10):
            final = [j] * b
            num = int("".join(str(e) for e in final))
            if num >= A and num <= B:
                ans += 1
        b -= 1
    return ans


def getUniformIntegerCountInInterval(A: int, B: int) -> int:

    total = 0
    A_digits = str(A)
    A_fst = A_digits[0]
    A_len = len(A_digits)
    A_next = int(A_fst * A_len)
    A_fst = int(A_fst)
    if A > A_next:
        A_fst += 1
    B_digits = str(B)
    B_fst = B_digits[0]
    B_len = len(B_digits)
    B_next = int(B_fst * B_len)
    B_fst = int(B_fst)
    distance = B_len - A_len
    # print(f"D:{distance}")
    if distance > 0:
        fst_rem = 10 - A_fst
        total += fst_rem
        A_fst = 1
        A_len += 1
        # print(f"T{total}")
    if distance > 1:
        # print(f"{B_len} - {A_len}")
        total += (B_len - A_len) * 9
        A_fst = 1
    # print(f"{B_fst} - {A_fst}")
    total += B_fst - A_fst
    # print(f"{B} >= {B_next}")
    if B >= B_next and A <= B_next:
        total += 1
    return total


def brute():
    for i in range(1, 9999):
        for j in range(i, 9999):
            if getUniformIntegerCountInInterval(
                i, j
            ) != getUniformIntegerCountInIntervalB(i, j):
                print(f"{i}, {j}, {getUniformIntegerCountInInterval(i,j)}")
                sys.exit(1)
        # print("BEEP")


def tests():

    A = 12
    B = 20
    print(getUniformIntegerCountInInterval(A, B) == 0)
    # sys.exit(1)
    A = 75
    B = 85
    print(getUniformIntegerCountInInterval(A, B) == 1)

    A = 33332
    B = 444433
    print(getUniformIntegerCountInInterval(A, B) == 10)
    # sys.exit(1)
    A = 0
    B = 1
    print(getUniformIntegerCountInInterval(A, B) == 2)

    A = 75
    B = 30000
    print(getUniformIntegerCountInInterval(A, B) == 23)

    A = 999999999999
    B = 999999999999
    print(getUniformIntegerCountInInterval(A, B) == 1)


tests()
brute()
