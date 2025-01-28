class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Arbitrarily picking first item in strs to compare all other strings against
        """
        longest_common_prefix = ""

        for idx in range(len(strs[0])):
            for word in strs:
                if idx + 1 > len(word) or word[idx] != strs[0][idx]:
                    return longest_common_prefix
            longest_common_prefix += strs[0][idx]

        return longest_common_prefix