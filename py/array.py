import unittest


def partialReverse(elements, start, end):
    for i in range((end - start) // 2 + 1):
        elements[start + i], elements[end - i] = elements[end - i], elements[start + i]
    return elements


class Test(unittest.TestCase):
    def test1(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(partialReverse(array, 2, 5), [1, 2, 6, 5, 4, 3, 7, 8, 9])

    def test2(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(partialReverse(array, 0, 8), [9, 8, 7, 6, 5, 4, 3, 2, 1])

    def test3(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(partialReverse(array, 2, 6), [1, 2, 7, 6, 5, 4, 3, 8, 9])


if __name__ == "__main__":
    unittest.main()
