from typing import List

# Write any import statements here


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    discs = len(R)
    defl = 0
    for i in range(discs - 1, 0, -1):
        # print(f"{R[i]} {R[i-1]}")
        if R[i] <= i:
            return -1
        if R[i] <= R[i - 1]:
            defl += 1
            R[i - 1] = R[i] - 1
    return defl


N = 5
R = [2, 5, 3, 6, 5]
print(getMinimumDeflatedDiscCount(N, R))

N = 3
R = [100, 100, 100]
print(getMinimumDeflatedDiscCount(N, R))

N = 4
R = [6, 5, 4, 3]
print(getMinimumDeflatedDiscCount(N, R))
