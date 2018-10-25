class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head_index = 0
        letter_tracker = set()
        max_length = 0

        for i, char in enumerate(s):
            while char in letter_tracker:
                head_char = s[head_index]
                letter_tracker.remove(head_char)
                head_index += 1

            letter_tracker.add(char)

            cur_length = i - head_index + 1
            if cur_length > max_length:
                max_length = cur_length

        return max_length




if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
