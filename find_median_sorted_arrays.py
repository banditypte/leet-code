class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        median_index = total_length / 2

        prev_value = None
        cur_value = None
        for i in range(0, int(median_index + 1)):
            prev_value = cur_value
            cur_value = list_to_chose_next(nums1, nums2).pop()

        if median_index == int(median_index):
            return (prev_value + cur_value) / 2
        return cur_value


def list_to_chose_next(l1, l2):
    if len(l1) == 0:
        if len(l2) == 0:
            return None
        return l2
    if len(l2) == 0:
        return l1

    if l1[-1] > l2[-1]:
        return l1
    return l2


if __name__ == '__main__':
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5

