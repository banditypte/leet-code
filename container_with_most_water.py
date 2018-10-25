class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height) - 1

        while i < j:
            i_height = height[i]
            j_height = height[j]
            area = min(i_height, j_height) * (j - i)

            if area > max_area:
                max_area = area

            if i_height < j_height:
                i += 1
            else:
                j -= 1

        return max_area


if __name__ == '__main__':
    assert Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) is 49
