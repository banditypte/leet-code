class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)

        return s == s[::-1]


if __name__ == '__main__':
    assert Solution().isPalindrome(42) is False
    assert Solution().isPalindrome(121) is True
    assert Solution().isPalindrome(-121) is False
