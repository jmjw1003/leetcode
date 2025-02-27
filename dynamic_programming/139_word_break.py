class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Approach is to iterate backwards through the string and see if it's
        possible to use a word starting from this position.
        Keep track of indexes where this is valid (+ True at the end as that
        is success).
        Time: O(n * m), space: O(n), where n is size of s, m is size of word dict.
        """
        valid_indexes = [False] * len(s) + [True]

        for idx in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # Check if word fits
                if len(word) + idx <= len(s) and s[idx: idx + len(word)] == word:
                    # If we can word break here, check if it ends on a valid
                    # index and update to True
                    valid_indexes[idx] = valid_indexes[idx + len(word)]
                if valid_indexes[idx]:
                    # If we can already reach the end from here,
                    # break out of the loop
                    break

        # If there was a possible solution, it should have been
        # backtracked to the start of the valid index array.
        return valid_indexes[0]
