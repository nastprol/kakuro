#!/usr/bin/env python3

import unittest
from Main import Main


class Test(unittest.TestCase):

    def test_4(self):
        t = Main()
        ans = t.main(4, 4, 'test1.txt')
        expected = ['X X X X X \nX 9 8 6 X \nX 8 1 3 X \nX 3 2 1 X \nX X X X X \n']
        self.assertListEqual(ans, expected)

    def test_5(self):
        t = Main()
        ans = t.main(5, 5, 'test3.txt')
        expected = ['X X X X X X \nX 8 4 X X X \nX 9 1 6 X X \nX X 2 9 1 X \nX X X 8 3 X \nX X X X X X \n']
        self.assertListEqual(ans, expected)

    def test_6(self):
        t = Main()
        ans = t.main(6, 6, 'test5.txt')
        expected = ['X X X X X X X \nX X 4 9 X X X \nX X 2 8 3 1 X \nX 1 3 X 4 2 X \nX 2 1 3 5 X X \nX X X 7 1 X X \nX X X X X X X \n']
        self.assertListEqual(ans, expected)

    def test_no_answer(self):
        t = Main()
        ans = t.main(4, 4, 'test2.txt')
        expected = []
        self.assertListEqual(ans, expected)

    def test_wrong_data(self):
        t = Main()
        ans = t.main(4, 4, 'test4.txt')
        expected = None
        self.assertEqual(ans, expected)


if __name__ == '__main__':
    unittest.main()