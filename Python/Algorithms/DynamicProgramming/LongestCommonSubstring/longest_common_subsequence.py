"""
Given two strings ‘X’ and ‘Y’, find the length of the longest common subsequence, which is not contiguous.
"""

class LongestCommonSubsequence:
    @staticmethod
    def find_longest_subsequence(s1: str, s2: str) -> str:
        len1 = len(s1)
        len2 = len(s2)
        if len1 == 0 or len2 == 0:
            return ''
        dp = [[0 for _ in range(len1)] for _ in range(len2)]
        max_len = 0
        max_len_index = None
        for j in range(len2):
            for i in range(len1):
                if s1[i] == s2[j]:
                    if i == 0 and j == 0:
                        dp[0][0] = 1
                    else:
                        dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

                if dp[j][i] > max_len:
                    max_len = dp[j][i]
                    max_len_index = (j, i)

        print(f'Longest subsequence is of length: {max_len}')
        if max_len > 0:
            j, i = max_len_index

            longest_str = ''
            while j >= 0 and i >= 0 and dp[j][i] >= 0:
                if dp[j][i] == 1 and (
                        (i == 0 and j == 0) or (i == 0 and dp[j - 1][i] == 0) or (j == 0 and dp[j][i - 1] == 0)
                        or (i != 0 and j != 0 and dp[j - 1][i - 1] == 0 and dp[j][i - 1] == 0 and dp[j - 1][i] == 0)):
                    longest_str = s1[i] + longest_str
                    break
                elif j > 0 and dp[j][i] == dp[j - 1][i]:
                    j = j - 1
                    continue
                elif i > 0 and dp[j][i] == dp[j][i - 1]:
                    i = i - 1
                    continue
                if j > 0 and i > 0 and dp[j][i] == dp[j - 1][i - 1] + 1:
                    longest_str = s1[i] + longest_str
                    j, i = j - 1, i - 1

            return longest_str

        return ''