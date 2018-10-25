# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            sum = l1_val + l2_val + carry
            newNode = ListNode(sum % 10)
            if head is None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode

            if sum >= 10:
                carry = 1
            else:
                carry = 0

            tail = newNode

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return head


def int_to_linked_list(number):
    l = int_to_list(number)
    prev_item = None
    for e in l:
        newNode = ListNode(e)
        newNode.next = prev_item
        prev_item = newNode

    return prev_item


def int_to_list(number):
    result = []

    while number > 0:
        result.insert(0, number % 10)
        number = int(number / 10)
    return result


def are_lists_equal(l1, l2):
    while list_has_next_item(l1) and list_has_next_item(l2):
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next

    if not list_has_next_item(l1) and not list_has_next_item(l2):
        return True
    return False


def list_has_next_item(l1):
    if l1.next is not None:
        return True
    return False


if __name__ == '__main__':
    assert int_to_list(125) == [1, 2, 5]
    assert int_to_list(3245) == [3, 2, 4, 5]

    l1 = int_to_linked_list(342)
    l2 = int_to_linked_list(465)
    result = Solution().addTwoNumbers(l1, l2)
    assert are_lists_equal(result, int_to_linked_list(807))

    l1 = int_to_linked_list(1)
    l2 = int_to_linked_list(0)
    result = Solution().addTwoNumbers(l1, l2)
    assert are_lists_equal(result, int_to_linked_list(1))

    l1 = int_to_linked_list(10)
    l2 = int_to_linked_list(1)
    result = Solution().addTwoNumbers(l1, l2)
    assert are_lists_equal(result, int_to_linked_list(11))

    l1 = int_to_linked_list(5)
    l2 = int_to_linked_list(5)
    result = Solution().addTwoNumbers(l1, l2)
    assert are_lists_equal(result, int_to_linked_list(10))
