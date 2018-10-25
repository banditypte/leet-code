class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        key = {
            '(': (True, ')'),
            '[': (True, ']'),
            '{': (True, '}'),
            ')': (False, '('),
            ']': (False, '['),
            '}': (False, '{'),
        }

        temp = ''
        for char in s:
            right_facing, op = key[char]
            if right_facing:
                temp += char
            else:
                if len(temp) == 0:
                    return False
                if temp[-1] == op:
                    temp = temp[0:-1]
                else:
                    return False

        return temp == ''


if __name__ == '__main__':
    assert Solution().isValid('()') is True
    assert Solution().isValid('(){}[]') is True
    assert Solution().isValid('(]') is False
    assert Solution().isValid('([)]') is False
    assert Solution().isValid('{[]}') is True
    assert Solution().isValid(']}') is False
