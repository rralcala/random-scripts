from typing import List

# Write any import statements here


def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    S = sorted(list(set(S)))
    ones = 0
    twos = 0
    # 1 -> 1
    # 2 -> 1,1 o 2
    # 3 -> 1,2
    # 4 -> 2,2
    # 5 -> 1,2,2
    # 6 -> 1,1,2,2 o 2,2,2
    for score in S:
        if score % 2 == 1:
            if ones == 0:
                ones = 1
            score -= 1
        if twos < score // 2:
            twos = score // 2

    return ones + twos


N = 4
S = [1, 3, 4]
print(getMinProblemCount(N, S))

N = 4
S = [4, 3, 3, 4]
print(getMinProblemCount(N, S))

N = 6
S = [1, 2, 3, 4, 5, 6]
print(getMinProblemCount(N, S))
