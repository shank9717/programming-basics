import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.LongestCommonSubstring.longest_common_subsequence import LongestCommonSubsequence


class TestLongestCommonSubsequence(TestCase):
    def setUp(self) -> None:
        self.lcs = LongestCommonSubsequence()

    def test_longest_subsequence_1(self):
        string1 = ''
        string2 = ''
        self.assertEqual('', self.lcs.find_longest_subsequence(string1, string2))

    def test_longest_subsequence_2(self):
        string1 = 'abc'
        string2 = 'de'
        self.assertEqual('', self.lcs.find_longest_subsequence(string1, string2))

    def test_longest_subsequence_3(self):
        string1 = 'a'
        string2 = 'abc'
        self.assertEqual('a', self.lcs.find_longest_subsequence(string1, string2))

    def test_longest_subsequence_4(self):
        string1 = 'abcd'
        string2 = 'ae'
        self.assertEqual('a', self.lcs.find_longest_subsequence(string1, string2))

    def test_longest_subsequence_5(self):
        string1 = 'abcd'
        string2 = 'abcd'
        self.assertEqual('abcd', self.lcs.find_longest_subsequence(string1, string2))

    def test_longest_subsequence_6(self):
        string1 = 'TestLongestSubstring:6thTest'
        string2 = 'ANewString:6thOne'
        self.assertEqual('eString:6the', self.lcs.find_longest_subsequence(string1, string2))

    def test_longest_subsequence_7(self):
        string1 = 'abcdaf'
        string2 = 'acbcf'
        self.assertEqual('abcf', self.lcs.find_longest_subsequence(string1, string2))


if __name__ == '__main__':
    unittest.main()
