import unittest
from collections import Counter

LONG_OUT = "hehehehehehehehehehehehehehehehehehehehehehehehehehehehcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmcmvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnvnfvyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfyfayawawawawawawawawawawawawawawawawawawawawawkukukukukukukukukukukukukukukukukukukukusksrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrsrxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpxpogogogogogogogogogogogogogogogogogtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtbidididididididididididididididzizlzlzlzlzlzlzlzlzlzlzljzjzqjqjqjqjqjqjqjqjqjqeq"
# LONG_OUT = "eweweweweweweweweweweweweweueueueueueueueueueueueueueueuhuhuhuhuhuhshshshshshshshshshshshshshshshshshshshphphphpcpcpcpcpcpcpcpcpcpcpcpcpcpcpcrcrcrcrcrcrcrcrcrcrcrcrmrmrmrmrmrmrmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmgmgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvovovovovovovovovonononononononononbnbnbnbnbnbnbnbnbnbnbnbnbnbnbabaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiatatatatatftftftftftftftftftftftfdfdfdfdfdfdfdfdfdfdfdydydydydyzyzyzyzyzyzyzyzyzyzyzyzyzyzyjyjyjyjkjkjkjkjkjkjkjklklklklklklklklklklklkqkqkqwqwqwqwqwqwqwqwq"
LONG_IN = "tndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxao"


class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) == 1:
            return S
        cnt = Counter(S)
        ordered = cnt.most_common()
        if len(ordered) == 1:
            return ""
        ret = []
        counters = {}
        for k in ordered:
            counters[k[0]] = k[1]

        a = ordered.pop(0)[0]
        b = ordered.pop(0)[0]
        while len(ordered) > 0 or (counters[b] and counters[a]):
            if counters[b] > counters[a]:
                a, b = b, a
            if counters[b] == 0:
                b = ordered.pop(0)[0]
                if counters[b] > counters[a]:
                    a, b = b, a
                continue

            while counters[b] > 0 and counters[a] > 0:
                ret.append(a)
                ret.append(b)
                counters[b] -= 1
                counters[a] -= 1

        while counters[a] > 0:
            if ret[-1] != a:
                ret.append(a)

            elif ret[0] != a and ret[0] != ret[-1]:
                ret.append(ret.pop(0))
                ret.append(a)
            else:
                return ""
            counters[a] -= 1

        ret_s = "".join(ret)
        if len(ret_s) != len(S):
            return ""
        return ret_s


class Tests(unittest.TestCase):
    def test1(self):
        self.assertEqual(
            "dadadabdcbc", Solution().reorganizeString("ddddaaabbcc")
        )  # dadadadbcbc

    def test2(self):
        self.assertEqual("aba", Solution().reorganizeString("aab"))

    def test3(self):
        self.assertEqual("", Solution().reorganizeString("aaab"))

    def test4(self):
        self.assertEqual("a", Solution().reorganizeString("a"))

    def test5(self):
        self.assertEqual("ababababab", Solution().reorganizeString("abbabbaaab"))

    def test6(self):
        self.maxDiff = None
        self.assertEqual(LONG_OUT, Solution().reorganizeString(LONG_IN))


if __name__ == "__main__":
    unittest.main()

"""            a = ordered[0][0]
            b = ordered[1][0]
            counters[ordered[0][0]] -= 1
            counters[ordered[1][0]] -= 1

            if counters[ordered[1][0]] == 0:
                del ordered[1]
            if counters[ordered[0][0]] == 0:
                del ordered[0]
            if len(ordered) >= 2 and counters[ordered[0][0]] < counters[ordered[1][0]]:
                ordered[0], ordered[1] = ordered[1], ordered[0]
            if len(ret) > 0 and a == ret[-1]:
                a,b = b,a
                if a == ret[-1]:
                    print(counters[ordered[0][0]])
                    print(ret)
                    return ""
            ret.append(a)
            ret.append(b)
        if len(ordered) == 1 and counters[ordered[0][0]] == 1 and ordered[0][0] != ret[-1]:
            ret.append(ordered[0][0])
            counters[ordered[0][0]] -= 1
            del ordered[0]
        elif len(ordered) > 0:
            print(f"{ordered[0][0]} {counters[ordered[0][0]]}")
            print(ret)
            return ""

        return "".join(ret)"""
