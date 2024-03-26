#!/bin/python
class jasstr:
    def __init__(self, data):
        # data, array of bytes [0x22, 0x40, 0x60, ...]
        self.data = data

    def print(self):
        print("".join([chr(byte) for byte in self.data]))

    def is_lower(self):
        for byte in self.data:
            # Check if the byte is upper case, if it is
            # bail out and return False.
            if byte >= 65 and byte <= 90:
                return False
        return True

    def is_digit(self):
        for byte in self.data:
            if byte >= 0x30 and byte <= 0x39:
                continue
            return False
        return True

    # TODO- IMPLEMENT ADD

    def addx(self, other):
        added_data = self.data + other.data
        return jasstr(added_data)

    # TODO- IMPLEMENT LEN

    def len(self):
        return len(self.data)

    # TODO- IMPLEMENT to_int
    def to_int(self):
        value = 0
        for byte in self.data:
            # Make sure the byte is a digit
            if byte < 0x31 or byte > 0x39:
                raise Exception("String has non-digit chars")
            digit_value = byte - 0x30
            value = (value * 10) + digit_value
        return value

    def add(self, rhs):
        result = ""
        for i in range(self.data.len()):
            digit1 = self.data[i] - 0x30
        for j in range(rhs):
            digit2 = rhs.data[j] - 0x30

            sum = digit1 + digit2
            if sum > 9:
                # first_digit  =
                second_digit = sum - digit1
                result += str(sum)


def add(str1, str2):
    result = ""
    max = max(len(str1), len(str2))
    complement = 0
    for i in range(max)[::-1]:
        if i >= str1.len():
            digit1 = 0
        else:
            digit1 = str1[i] - 0x30
        if i >= str2.len():
            digit2 = 0
        else:
            digit2 = str2[i] - 0x30
        sum = digit1 + digit2 + complement
        complement = 0
        if sum > 9:
            complement = 1
            sum -= 10
        result += str(sum)
    if complement != 0:
        result += str(1)
    return result[::-1]

    def binary_to_int(self):
        value = 0
        for byte in self.data:
            # Make sure the byte is a digit
            if byte < 0x31 or byte > 0x39:
                raise Exception("String has non-digit chars")
            digit_value = byte - 0x30
            value = (value * 2) + digit_value
        return value


def divide_str(str1, str2):
    result = ''
    divider = str1 - 0x30
    accumlator = 0
    for i in str2 - 0x30:
        if accumlator >= divider:
            quotient = accumlator // divider
            accumlator = accumlator % divider
            result += str(quotient)

        digit = str2[i] - 0x30
        accumlator += (accumlator * 10) + digit
    if accumlator != 0:
        result += str(accumlator // 10)
    return result


result = divide_str('5', '345')
print(result)


# TODO- impliment devide with 2 intigers, we assume that user puts two intigers therfore we will not write exceptions with value errors.

def divide_int(int1, int2):
    result = ''
    divider = int1
    accumlator = 0
    for i in range(int2):
        if accumlator >= divider:
            quotient = accumlator // int1
            accumlator = accumlator % int1
            result += str(quotient)
        digit = int2[i]
        accumlator += (accumlator * 10) + digit
        if accumlator != 0:
            result += accumlator // 10
    return result


result = divide_int(89, 345)
print(result)



#TODO- IMPLIMENT PRINT_DIV WITH INTIGERS

def print_div(dividend, divisor):
    if divisor == 0:
        raise Exception('you cannot divide by zero! ')
        return
    quotient = dividend // divisor
    remainder = dividend % divisor
    result = str(quotient)
    if remainder != 0:
        result += '.'
        decimal_places = 0 #digits after the dot
        while remainder != 0 and decimal_places < 6:
            remainder *= 10
            quotient = remainder // divisor
            result += str(quotient)
            remainder %= divisor
            decimal_places += 1

    print(result)

#deleted the other files.


if __name__ == "__main__":
    a = jasstr([0x36, 0x31, 0x32, 0x33, 0x69, 0x41])
    b = jasstr([0x41, 0x32, 0x33, 0x34, 0x69, 0x40])
    a.print()
    print(a.is_lower())
    c = a.add(b)
    c.print()
    print(a.len())
    print(a.to_int())

