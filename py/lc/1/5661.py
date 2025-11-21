import unittest


class Solution:
    def maximumTime(self, time: str) -> str:
        hr_s, min_s = time.split(":")

        return f"{self.max_hr(hr_s)}:{self.max_min(min_s)}"

    def max_min(self, min_s: str) -> str:

        res = []
        if min_s[0] == "?":
            res.append("5")
        else:
            res.append(min_s[0])
        if min_s[1] == "?":
            res.append("9")
        else:
            res.append(min_s[1])
        return "".join(res)

    def max_hr(self, hr: str) -> str:

        res = []
        if len(hr) == 2:
            if hr[0] == "?":
                if hr[1] == "?" or int(hr[1]) < 4:
                    res.append("2")
                else:
                    res.append("1")
            else:
                res.append(hr[0])

            if hr[1] == "?":
                if res[0] == "2":
                    res.append("3")
                else:
                    res.append("9")
            else:
                res.append(hr[1])
        else:
            if hr[0] == "?":
                res.append("9")
            else:
                res.append(hr[0])

        return "".join(res)


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(Solution().maximumTime("1?:22"), "19:22")
        self.assertEqual(Solution().maximumTime("?:??"), "9:59")
        self.assertEqual(Solution().maximumTime("??:??"), "23:59")
        self.assertEqual(Solution().maximumTime("2?:??"), "9:59")


unittest.main()
