import unittest
from unittest import TestCase

from Algorithms.DynamicProgramming.LongestCommonSubstring.longest_common_substring import LongestCommonSubstring


class TestLongestCommonSubstring(TestCase):
    def setUp(self) -> None:
        self.lcs = LongestCommonSubstring()

    def test_longest_substring_1(self):
        string1 = ''
        string2 = ''
        self.assertEqual('', self.lcs.find_longest_substring(string1, string2))

    def test_longest_substring_2(self):
        string1 = 'abc'
        string2 = 'de'
        self.assertEqual('', self.lcs.find_longest_substring(string1, string2))

    def test_longest_substring_3(self):
        string1 = 'a'
        string2 = 'abc'
        self.assertEqual('a', self.lcs.find_longest_substring(string1, string2))

    def test_longest_substring_4(self):
        string1 = 'abcd'
        string2 = 'ae'
        self.assertEqual('a', self.lcs.find_longest_substring(string1, string2))

    def test_longest_substring_5(self):
        string1 = 'abcd'
        string2 = 'abcd'
        self.assertEqual('abcd', self.lcs.find_longest_substring(string1, string2))

    def test_longest_substring_6(self):
        string1 = 'TestLongestSubstring:6thTest'
        string2 = 'ANewString:6thOne'
        self.assertEqual('tring:6th', self.lcs.find_longest_substring(string1, string2))


if __name__ == '__main__':
    unittest.main()
