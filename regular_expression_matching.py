class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        char_to_match = ''
        repeating = False
        for char in s[::-1]:
            if not repeating:
                if len(p) == 0:
                    return False
                (char_to_match, repeating, p) = get_next_op(p)
            if char_to_match is not char and char_to_match is not '.':
                if repeating:
                    repeating = False
                else:
                    return False

        return True


def get_next_op(p):
    repeating = False
    while p[-1] is '*':
        repeating = True
        p = p[:-1]
    return p[-1], repeating, p[:-1]


if __name__ == '__main__':
    assert Solution().isMatch('aa', 'a') is False
    assert Solution().isMatch('aa', 'a*') is True
    assert Solution().isMatch('ab', '.*') is True
    assert Solution().isMatch('aab', 'c*a*b') is True
    assert Solution().isMatch('mississippi', 'mis*is*p*.') is False
    assert Solution().isMatch('ab', '.*c') is False
    assert Solution().isMatch('aaba', 'ab*a*c*a') is False
