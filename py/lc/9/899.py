class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            elements = list(S)
            comp = list(S)
            comp.append(comp.pop(0))
            for _ in range(len(S)):
                if comp < elements:
                    elements = list(comp)
                comp.append(comp.pop(0))
            return "".join(elements)
        else:
            return "".join(sorted(S))


print(Solution().orderlyQueue("cba", 1))
print(Solution().orderlyQueue("baaca", 3))
