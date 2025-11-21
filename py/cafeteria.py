# Write any import statements here
import math
from typing import List


def available_s(p, n, k):
    if n - p == 1:
        return 0
    v = (n - (p)) / (1 + k)
    return v


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    S = sorted(S)
    seats = 0
    next_blocked = 0
    for i, _ in enumerate(S):

        if i == 0:
            next_blocked = S[i] - K
            # print(next_blocked)
            if next_blocked <= 1:
                continue
            else:
                pb = 1 if S[i] == 1 else 0
                seats += math.floor(available_s(pb, next_blocked, K))
                # print(f"s {seats}")
        else:
            next_blocked = S[i] - K
            prev_blocked = S[i - 1] + K
            available = math.floor(available_s(prev_blocked, next_blocked, K))
            if available > 0:
                seats += available
    last = math.floor(available_s(next_blocked + K, N, K))
    if last > 0:
        seats += last

    return seats


N = 10
K = 1
M = 2
S = [2, 6]
print(getMaxAdditionalDinersCount(N, K, M, S) == 3)

N = 10
K = 1
M = 2
S = [1, 10]
print(getMaxAdditionalDinersCount(N, K, M, S) == 3)

N = 11
K = 1
M = 2
S = [1, 11]
print(getMaxAdditionalDinersCount(N, K, M, S) == 4)

N = 15
K = 2
M = 3
S = [11, 6, 14]
print(getMaxAdditionalDinersCount(N, K, M, S) == 1)

N = 15
K = 0
M = 0
S = []
print(getMaxAdditionalDinersCount(N, K, M, S) == 15)

N = 3
K = 0
M = 0
S = [1, 2, 3]
print(getMaxAdditionalDinersCount(N, K, M, S) == 0)

N = 0
K = 0
M = 0
S = []
print(getMaxAdditionalDinersCount(N, K, M, S) == 0)
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
#       [        ][           ]
