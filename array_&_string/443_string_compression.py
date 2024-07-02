class Solution:
    def compress(self, chars: list[str]) -> int:
        count_ = 0
        current_char = chars[0]
        s = ""
        for i in range(len(chars)):
            if chars[i] == current_char:
                count_ += 1
            else:
                s += current_char if count_ == 1 else current_char + str(count_)
                count_ = 1
            current_char = chars[i]
        s += current_char if count_ == 1 else current_char + str(count_)
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
    

# Not using any extra space
class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0
        
            # Count occurence of char
            while read<len(chars) and chars[read] == char:
                read += 1
                count += 1

            # write that char to write pos
            chars[write] = char
            write += 1

            # If the char count is more than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write