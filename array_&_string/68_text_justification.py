class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        output = []

        curr_line = [words[0]]
        curr_length = len(words[0])
        for word in words[1:]:
            # Check if word fits and add
            if len(word) + (1 * len(curr_line)) + curr_length <= maxWidth:
                curr_length += len(word)
                curr_line.append(word)
            # Word is too big to fit
            else:
                # Check if extra padding required
                space_remaining = maxWidth - curr_length - ((1 * len(curr_line)) - 1)
                # Apply extra padding
                idx = 0
                while space_remaining > 0:
                    # Final word must be on right border
                    # If one word will instead append " "
                    if idx >= len(curr_line) - 1:
                        idx = 0
                    curr_line[idx] += " "
                    space_remaining -= 1
                    idx += 1
                # Add curr_line to output
                output.append(" ".join(curr_line))

                # Create new curr_line using word
                curr_line = [word]
                curr_length = len(word)
        
        # Pad final line
        final_line = " ".join(curr_line)
        final_line += " " * (maxWidth - len(final_line))
        output.append(final_line)
        return output


s = Solution()

# words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

x = s.fullJustify(words, maxWidth)

for i in x:
    print("|", i, "|")