# Write any import statements here


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    sets = 0
    if len(C) < 3:
        return sets
    for i, v in enumerate(C):
        if v == "A":

            start = i - Y
            if start < 0:
                start = 0
            end = i - (X - 1)
            if end < 0:
                end = 0
            left = C[start:end]

            start = i + X
            if start > len(C):
                start = len(C)
            end = i + Y + 1

            if end > len(C):
                end = len(C)

            right = C[start:end]
            P_on_left = left.count("P")
            B_on_left = left.count("B")
            P_on_right = right.count("P")
            B_on_right = right.count("B")
            sets += P_on_left * B_on_right + B_on_left * P_on_right

    return sets


N = 8
C = ".PBAAP.B"
X = 1
Y = 3

print(getArtisticPhotographCount(N, C, X, Y) == 3)

N = 5
C = "APABA"
X = 2
Y = 3
print(getArtisticPhotographCount(N, C, X, Y) == 0)

N = 5
C = "APABA"
X = 1
Y = 2

print(getArtisticPhotographCount(N, C, X, Y) == 1)

N = 5
C = ".........."
X = 1
Y = 2

print(getArtisticPhotographCount(N, C, X, Y) == 0)

N = 3
C = "AB."
X = 1
Y = 2

print(getArtisticPhotographCount(N, C, X, Y) == 0)
