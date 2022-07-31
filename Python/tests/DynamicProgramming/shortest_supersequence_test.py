import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.LongestCommonSubstring.shortest_common_supersequence import \
    ShortestCommonSupersequence


class TestLongestCommonSubsequence(TestCase):
    def setUp(self) -> None:
        self.scs = ShortestCommonSupersequence()

    def assertSubsequence(self, string: str, supersequence: str):
        if len(string) == 0:
            return
        idx = 0
        for j in range(len(supersequence)):
            if string[idx] == supersequence[j]:
                idx += 1
                if idx == len(string):
                    break
        else:
            self.fail(f'{supersequence} is not a supersequence of {string}')

    def shortest_sequence_tester(self, string1: str, string2: str, known_supersequence: str):
        self.assertSubsequence(string1, known_supersequence)
        self.assertSubsequence(string2, known_supersequence)

        res = self.scs.shortest_common_supersequence(string1, string2)
        self.assertSubsequence(string1, res)
        self.assertSubsequence(string2, res)
        self.assertEqual(len(known_supersequence), len(res))

    def test_shortest_supersequence_1(self):
        self.shortest_sequence_tester('', '', '')

    def test_shortest_supersequence_2(self):
        self.shortest_sequence_tester('abac', 'cab', 'cabac')

    def test_shortest_supersequence_3(self):
        self.shortest_sequence_tester('bbbaaaba', 'bbababbb', 'bbabaaababb')

    def test_shortest_supersequence_4(self):
        self.shortest_sequence_tester('bcacaaab', 'bbabaccc', 'bbabacacaaabc')

    def test_shortest_supersequence_5(self):
        self.shortest_sequence_tester('ababaabbbb', 'cbcbacaab', 'acbcbabcaabbbb')

    def test_shortest_supersequence_6(self):
        self.shortest_sequence_tester('a', '', 'a')

    def test_shortest_supersequence_6(self):
        self.shortest_sequence_tester('a', 'a', 'a')


if __name__ == '__main__':
    unittest.main()
