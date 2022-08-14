class ShortestCommonSupersequence:
    @staticmethod
    def shortest_common_supersequence(str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        dp = [[0 for _ in range(len1)] for _ in range(len2)]

        max_index = None
        longest_seq_len = 0

        for j in range(len2):
            for i in range(len1):
                if str1[i] == str2[j]:
                    if i == 0 or j == 0:
                        dp[j][i] = 1
                    else:
                        dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])

                if dp[j][i] > longest_seq_len:
                    longest_seq_len = dp[j][i]
                    max_index = (j, i)

        if longest_seq_len == 0:
            return str1 + str2

        longest_seq = ''
        (j, i) = max_index
        while j >= 0 and i >= 0 and dp[j][i] >= 0:
            if dp[j][i] == 1 and (
                    (i == 0 and j == 0) or (i == 0 and dp[j - 1][i] == 0) or (j == 0 and dp[j][i - 1] == 0)
                    or (i != 0 and j != 0 and dp[j - 1][i - 1] == 0 and dp[j][i - 1] == 0 and dp[j - 1][i] == 0)):
                longest_seq = str1[i] + longest_seq
                break
            elif j > 0 and dp[j][i] == dp[j - 1][i]:
                j = j - 1
                continue
            elif i > 0 and dp[j][i] == dp[j][i - 1]:
                i = i - 1
                continue
            if j > 0 and i > 0 and dp[j][i] == dp[j - 1][i - 1] + 1:
                longest_seq = str1[i] + longest_seq
                j, i = j - 1, i - 1

        i = 0
        j = 0
        k = 0
        shortest_subsequence = ''
        while i < len1 and j < len2 and k < len(longest_seq):
            if str1[i] == str2[j] == longest_seq[k]:
                shortest_subsequence += longest_seq[k]
                i += 1
                j += 1
                k += 1
                continue
            if str1[i] == longest_seq[k]:
                shortest_subsequence += str2[j]
                j += 1
            elif str2[j] == longest_seq[k]:
                shortest_subsequence += str1[i]
                i += 1
            else:
                shortest_subsequence += str1[i] + str2[j]
                i, j = i + 1, j + 1

        while i < len1:
            shortest_subsequence += str1[i]
            i += 1
        while j < len2:
            shortest_subsequence += str2[j]
            j += 1
        return shortest_subsequence