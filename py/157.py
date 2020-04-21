import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s = s.lower()
        regex = re.compile('[^a-z0-9]')

        s = regex.sub('', s)
        print(s)

        return s == ''.join(reversed(s))


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))