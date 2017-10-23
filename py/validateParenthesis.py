class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for c in s:
            if c == '{' or c == '[' or c == '(':
                l.append(c)
            if c == ']':
                if len(l) == 0 or l.pop() != '[':
                    return False
            if c == ')':
                if len(l) == 0 or l.pop() != '(':
                    return False
            if c == '}':
                if len(l) == 0 or l.pop() != '{':
                    return False

        if len(l) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid("()[]{}"))
print(s.isValid("(()"))

print(s.isValid("]"))

