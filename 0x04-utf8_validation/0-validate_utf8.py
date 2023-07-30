#!/usr/bin/python3
'''A method to validate whether a given data set represents
   a valid UTF-8 encoding.
   '''

def validUTF8(data):
    # Initializing a variable to keep track of the number of continuation bytes needed.
    num_continuation_bytes = 0

    # Looping through each byte in the data list.
    for byte in data:
        # Checking if the current byte is a continuation byte (10xxxxxx).
        if byte & 0b11000000 == 0b10000000:
            # If it's a continuation byte, decrease the count of needed continuation bytes.
            num_continuation_bytes -= 1
        else:
            # Checking the number of bytes needed for the current character.
            # The leading bits of the byte determine the number of bytes needed.
            if byte & 0b11110000 == 0b11110000:
                num_continuation_bytes = 3
            elif byte & 0b11100000 == 0b11100000:
                num_continuation_bytes = 2
            elif byte & 0b11000000 == 0b11000000:
                num_continuation_bytes = 1
            elif byte & 0b10000000 == 0b00000000:
                num_continuation_bytes = 0
            else:
                # If the byte doesn't match any valid pattern, it's not a valid UTF-8 encoding.
                return False

            # Checking if the number of continuation bytes needed is greater than the remaining data.
            if num_continuation_bytes > len(data) - 1:
                return False

    # After processing all bytes, if there are still continuation bytes needed, it's not a valid encoding.
    return num_continuation_bytes == 0