from typing import List

# Write any import statements here


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    return N - min(P)


N = 6
F = 3
P = [5, 2, 4]
print(getSecondsRequired(N, F, P))

N = 3
F = 1
P = [1]
print(getSecondsRequired(N, F, P))

N = 6
F = 3
P = [1, 3, 5]
print(getSecondsRequired(N, F, P))
