from typing import Optional


class ListNode:
    def __init__(self, val=0, next_val=None):
        self.val = val
        self.next = next_val


class Solution:
    @staticmethod
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        tail = result

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = list1
                list1 = list1.next
            else:
                tail.next = list2
                tail = list2
                list2 = list2.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return result.next


if __name__ == '__main__':
    print(Solution.mergeTwoLists([1, 2, 4], [1, 3, 4]))
