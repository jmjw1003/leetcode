class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge cases
        if len(t) > len(s) or t == "":
            return ""
        
        # Counter of characters in t and current window of s
        t_counter, window = {}, {}
        for char in t:
            t_counter[char] = t_counter.get(char, 0) + 1
        
        # characters we need vs have
        have, need = 0, len(t_counter)

        # return value
        min_window, min_length = "", float("inf")

        # Iterate through s
        l = 0  # l = left pointer, r = right pointer
        for r in range(len(s)):
            # Add char to window counter
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # Check if match with requirements from t
            if c in t_counter and window[c] == t_counter[c]:
                have += 1
            
            # If all requirements fulfilled
            while have == need:
                # Update result
                if (r + 1 - l) < min_length:
                    min_window = s[l:r + 1]
                    min_length = r + 1 - l
                # Shrink window
                window[s[l]] -= 1
                if s[l] in t_counter and window[s[l]] < t_counter[s[l]]:
                    have -= 1
                l += 1
        
        return min_window
        
