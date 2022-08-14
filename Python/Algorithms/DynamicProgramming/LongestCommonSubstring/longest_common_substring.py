"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
"""

class LongestCommonSubstring:
    @staticmethod
    def find_longest_substring(s1: str, s2: str) -> str:
        len1 = len(s1)
        len2 = len(s2)
        if len1 == 0 or len2 == 0:
            return ''
        dp = [[0 for _ in range(len2)] for _ in range(len1)]
        max_len = 0
        max_len_index = None
        for i in range(len1):
            for j in range(len2):
                if s1[i] == s2[j]:
                    if i == 0 and j == 0:
                        dp[0][0] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                        max_len_index = (i, j)
                else:
                    dp[i][j] = 0

        print(f'Longest substring is of length: {max_len}')
        if max_len > 0:
            longest_str = ''
            indices = max_len_index
            while indices[0] >= 0 and indices[1] >= 0 and dp[indices[0]][indices[1]] != 0:
                longest_str = s1[indices[0]] + longest_str
                indices = (indices[0] - 1, indices[1] - 1)

            return longest_str

        return ''