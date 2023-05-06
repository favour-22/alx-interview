#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: a list of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    # Step 1: Define helper functions to check the leading bits of a byte
    def is_1byte(code):
        return (code & 0b10000000) == 0b00000000

    def is_2byte(code):
        return (code & 0b11100000) == 0b11000000

    def is_3byte(code):
        return (code & 0b11110000) == 0b11100000

    def is_4byte(code):
        return (code & 0b11111000) == 0b11110000

    # Step 2: Iterate over the input data and check each byte
    i = 0
    while i < len(data):
        if is_1byte(data[i]):
            # 1-byte character
            i += 1
        elif is_2byte(data[i]):
            # 2-byte character
            if i + 1 >= len(data) or not is_1byte(data[i + 1]):
                return False
            i += 2
        elif is_3byte(data[i]):
            # 3-byte character
            if i + 2 >= len(data) or not is_1byte(data[i + 1]) or not is_1byte(data[i + 2]):
                return False
            i += 3
        elif is_4byte(data[i]):
            # 4-byte character
            if i + 3 >= len(data) or not is_1byte(data[i + 1]) or not is_1byte(data[i + 2]) or not is_1byte(data[i + 3]):
                return False
            i += 4
        else:
            # Invalid leading byte
            return False

    # Step 3: All bytes have been checked and no invalid sequences were found
    return True
