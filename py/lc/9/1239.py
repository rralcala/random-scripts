from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        offset = ord("a")
        selected = []
        for member in arr:
            bitmap = 0
            add = True
            for char in member:
                pos = ord(char) - offset
                if bitmap & 1 << pos:
                    add = False
                    break
                bitmap = bitmap | 1 << pos

            # Could be a colision or not
            if add:
                for i in range(len(selected)):
                    if bitmap & selected[i][1] == 0:
                        pass
                    elif len(member) > len(selected[i][0]):
                        selected[i] = (member, bitmap)
                        add = False
                    else:
                        add = False
                if add:
                    selected.append((member, bitmap))
        sum = 0
        print(selected)
        for item in selected:
            sum += len(item[0])

        return sum


assert Solution().maxLength(["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]) == 11
assert Solution().maxLength(["un", "iq", "ue"]) == 4
assert Solution().maxLength(["ca", "r", "act", "ers"]) == 6
assert Solution().maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26
assert Solution().maxLength(["aa", "bb"]) == 0
