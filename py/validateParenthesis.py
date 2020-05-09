class Solution(object):
    @staticmethod
    def is_valid(stack):
        l = []
        for c in stack:
            if c == "{" or c == "[" or c == "(":
                l.append(c)
            if c == "]":
                if len(l) == 0 or l.pop() != "[":
                    return False
            if c == ")":
                if len(l) == 0 or l.pop() != "(":
                    return False
            if c == "}":
                if len(l) == 0 or l.pop() != "{":
                    return False

        if len(l) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()[]{}"))
    print(s.isValid("(()"))

    print(s.isValid("]"))
