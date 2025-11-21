class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        characters = len(columnTitle)
        start = ord("A") - 1
        end = ord("Z") - start
        val = 0
        for i in range(characters):
            pos = characters - i - 1
            val += pow(end, pos) * (ord(columnTitle[i]) - start)
        return val


s = Solution()
print(s.titleToNumber("AB"))
print(s.titleToNumber("FXSHRXW"))
