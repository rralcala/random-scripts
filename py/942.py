from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        end = len(S)
        start = 0
        out = []
        for op in S:
            if op == "D":
                out.append(end)
                end -= 1
            else:
                out.append(start)
                start += 1

        return out + [start]


print(Solution().diStringMatch("DDI"))
