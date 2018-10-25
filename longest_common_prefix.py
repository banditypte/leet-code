class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        prefix = strs[0]
        for string in strs[1:]:
            cur_prefix = ''
            for i_char, char in enumerate(prefix):
                if i_char > len(string) - 1:
                    break
                if char is not string[i_char]:
                    break
                cur_prefix += char
            prefix = cur_prefix
            if len(prefix) == 0:
                break
        return prefix


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'
    assert Solution().longestCommonPrefix(['dog', 'racecar', 'car']) == ''
    assert Solution().longestCommonPrefix([]) == ''
