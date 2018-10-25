class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        max_palindrome = ''

        for x in range(0, len(s)):
            largest_current_palindrome = largest_palindrome_at_index(s, x)
            if len(largest_current_palindrome) > max_length:
                max_length = len(largest_current_palindrome)
                max_palindrome = largest_current_palindrome

        return max_palindrome


def is_palindrome(s):
    return s == s[::-1]


def largest_palindrome_at_index(s, i):
    x = i
    while x > 0 and s[x] == s[x - 1]:
        x -= 1

    y = i + 1
    while y < len(s) - 1 and s[y - 1] == s[y]:
        y += 1

    largest_palindrome = ''
    while x >= 0 and y <= len(s):
        sub_string = s[x:y]
        if is_palindrome(sub_string):
            largest_palindrome = sub_string
        else:
            break
        x -= 1
        y += 1

    return largest_palindrome


def b_1000():
    s = ''
    for i in range(0, 1000):
        s += 'b'
    return s



if __name__ == '__main__':
    assert is_palindrome('racecar') is True
    assert is_palindrome('hello') is False

    assert largest_palindrome_at_index('aba', 1) == 'aba'
    assert largest_palindrome_at_index('aba', 0) == 'a'
    assert largest_palindrome_at_index('abba', 1) == 'abba'
    assert largest_palindrome_at_index('abba', 2) == 'abba'

    assert Solution().longestPalindrome('a') == 'a'
    assert Solution().longestPalindrome('babad') == 'bab'
    assert Solution().longestPalindrome('cbbd') == 'bb'
    assert Solution().longestPalindrome('cbbdasldkfjalksdjfinsasdkfjsoidnfsoidfnsodifnsodifndifsldfsidoifns') == 'sas'
    assert Solution().longestPalindrome(b_1000()) == b_1000()
