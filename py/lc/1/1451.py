import unittest


class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        words = text.split()
        words.sort(key=lambda x: len(x))
        text = " ".join(words)
        return text[0].upper() + text[1:]


class TestCases(unittest.TestCase):
    def test(self):
        self.assertEqual("Keep calm and code on", "On and keep calm code")
        self.assertEqual("Leetcode is cool", "Is cool leetcode")
        self.assertEqual("To be or not to be", "To be or to be not")
