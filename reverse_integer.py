class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)

        negative = False
        if s[0] == '-':
            negative = True

        i_first_number = 1 if negative else 0

        reversed_number = s[i_first_number:][::-1]

        result_string = '-' + reversed_number if negative else reversed_number

        result = int(result_string)

        if abs(result) > 2 ** 31 - 1:
            return 0

        return result


if __name__ == '__main__':
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(1534236469) == 0
    assert Solution().reverse(1563847412) == 0
