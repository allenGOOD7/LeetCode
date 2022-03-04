from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_longest = max(strs)
        str_shortest = min(strs)
        for i in range(len(str_shortest)):
            if (str_longest[i] != str_shortest[i]):
                return str_shortest[:i]
        return str_shortest