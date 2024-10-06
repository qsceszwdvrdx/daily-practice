# Python script for LeetCode problems
class Solution:
    def compress(self, chars: list[str]) -> int:
        write_index = 0  # Pointer for the position to write in the array
        read_index = 0   # Pointer for reading the array
        
        while read_index < len(chars):
            current_char = chars[read_index]  # The character to count
            count = 0  # Count of the current character
            
            # Count the number of consecutive occurrences
            while read_index < len(chars) and chars[read_index] == current_char:
                read_index += 1
                count += 1
            
            # Write the current character to the array
            chars[write_index] = current_char
            write_index += 1
            
            # If the count is greater than 1, we need to write it too
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index  # The new length of the compressed array