from typing import List


class KnuthMorissPratt:
    @staticmethod
    def search_pattern(main_string: str, pattern: str) -> int:
        lps_arr = KnuthMorissPratt.get_lps_array(pattern)
        i, j = 0, 0
        while i < len(main_string):
            if main_string[i] == pattern[j]:
                i, j = i + 1, j + 1
                if j == len(pattern):
                    return i - j
                continue
            if j != 0:
                j = lps_arr[j - 1]
            else:
                i += 1
        return -1

    @staticmethod
    def get_lps_array(pattern: str) -> List[int]:
        i = 1
        j = 0
        lps_arr = [0] * len(pattern)

        while i < len(lps_arr):
            if pattern[j] == pattern[i]:
                lps_arr[i] = j + 1
                i, j = i + 1, j + 1
            else:
                if j != 0:
                    j = lps_arr[j - 1]
                else:
                    lps_arr[i] = 0
                    i += 1

        return lps_arr
