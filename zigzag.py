class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ''
        skips = get_skips(numRows)
        for i, skip in enumerate(skips):
            result += s[i::skip]

        return result


def get_skips(num_rows):
    if num_rows == 1:
        return [1]
    a = []
    for i in range(num_rows):
        a.append(0)

    x = int((num_rows - 1) / 2)
    y = x if x == (num_rows - 1) / 2 else x + 1

    skips = int(num_rows / 2) * 2

    while x >= 0 and y < len(a):
        a[x] = skips
        a[y] = skips
        x -= 1
        y += 1
        skips += 2

    return a


if __name__ == '__main__':
    assert get_skips(1) == [1]
    assert get_skips(2) == [2, 2]
    assert get_skips(3) == [4, 2, 4]
    assert get_skips(4) == [6, 4, 4, 6]

    assert Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert Solution().convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
    assert Solution().convert('abc', 1) == 'abc'
