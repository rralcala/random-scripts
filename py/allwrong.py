N = 5
C = "ABABAB"


def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    R = []
    for row in G:

        if C[i] == "A":
            R.append("B")
        else:
            R.append("A")
    return "".join(R)


print(getWrongAnswers(N, C))
