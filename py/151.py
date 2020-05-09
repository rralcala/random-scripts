class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        out = []
        for w in a:
            if w != "":
                out.append(w)
        return " ".join(reversed(out))


print(Solution().reverseWords("  hello world!  ") == "world! hello")
print(Solution().reverseWords("the sky is blue") == "blue is sky the")
print(Solution().reverseWords("a good   example") == "example good a")
