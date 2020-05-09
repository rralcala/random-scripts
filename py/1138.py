class Solution:

    @staticmethod
    def charval(char: str) -> int:
        return ord(char) - ord('a')

    @staticmethod
    def sign(x: int) -> int:
        if x < 0:
            return -1
        return 1

    def alphabetBoardPath(self, target: str) -> str:
        target = target.lower()
        result = ""
        pos = 0
        zee = False
        for char in target:

            if char == 'z' and not zee:
                char = 'u'
                zee = True
            else:
                zee = False
            t = self.charval(char)
            distance = int(t / 5) - int(pos / 5)

            if distance > 0:
                result += "D" * distance
            elif distance < 0:
                result += "U" * abs(distance)
            pos += distance * 5

            distance = self.sign(t-pos) * (abs((t-pos)) % 5)

            if distance > 0:
                result += "R" * distance
            elif distance < 0:
                result += "L" * abs(distance)
            pos = t
            if zee:
                result += 'D'
                pos += 5

            result += "!"
        return result


print(Solution().alphabetBoardPath('leet') == 'DDR!UURRR!!DDD!')
print(Solution().alphabetBoardPath('code') == 'RR!DDRR!UUL!R!')
print(Solution().alphabetBoardPath('zdz') == 'DDDDD!UUUUURRR!DDDDLLLD!')
print(Solution().alphabetBoardPath('zzuz') == 'DDDDD!!U!D!')
