class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # remove whitespace
        str = str.strip()

        if len(str) < 1:
            return 0

        negative = False
        if str[0] == '-':
            negative = True
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]

        if not str:
            return 0

        temp_int = 0
        for c in str:
            int_value = ord(c) - 48
            if int_value < 0 or int_value > 9:
                break
            temp_int = temp_int * 10
            temp_int += int_value

        if negative:
            temp_int = -temp_int

        if temp_int > 2 ** 31 - 1:
            temp_int = 2 ** 31 - 1
        if temp_int < -(2 ** 31):
            temp_int = -(2 ** 31)

        return temp_int


if __name__ == '__main__':
    assert Solution().myAtoi('42') == 42
    assert Solution().myAtoi('   -42') == -42
    assert Solution().myAtoi('4193 with words') == 4193
    assert Solution().myAtoi('words and 987') == 0
    assert Solution().myAtoi('-91283472332') == -2147483648
    assert Solution().myAtoi('91283472332') == 2 ** 31 - 1
    assert Solution().myAtoi('') == 0
    assert Solution().myAtoi('-') == 0
    assert Solution().myAtoi('+') == 0
