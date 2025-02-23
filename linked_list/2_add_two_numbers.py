from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Efficient solution: Iterate through two linked lists at the same time, adding the values* and 
        writing to the existing linked lists.
        * Second digit is carried over to the next node.
        If one list remains after iteration the process continues while a carry over 1 remains.
        Longer list head is then returned.
        Time: O(n) - Linear iteration through linked lists.
        Space: O(1) - Only storing a few extra variables.
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        curr1, curr2, carry_over = l1, l2, 0
        while curr1 and curr2:
            val = curr1.val + curr2.val + carry_over
            if val > 9:
                val = val % 10
                carry_over = 1
            else:
                carry_over = 0
            curr1.val = val
            curr2.val = val
            if not curr1.next and not curr2.next and carry_over:
                curr1.next = ListNode(1)
                return l1
            curr1 = curr1.next
            curr2 = curr2.next

        if not curr2:
            while carry_over:
                val = curr1.val + carry_over
                if val > 9:
                    val = val % 10
                    carry_over = 1
                else:
                    carry_over = 0
                curr1.val = val
                if carry_over:
                    if curr1.next:
                        curr1 = curr1.next
                    else:
                        curr1.next = ListNode(1)
                        carry_over = 0
            return l1

        if not curr1:
            while carry_over:
                val = curr2.val + carry_over
                if val > 9:
                    val = val % 10
                    carry_over = 1
                else:
                    carry_over = 0
                curr2.val = val
                if carry_over:
                    if curr2.next:
                        curr2 = curr2.next
                    else:
                        curr2.next = ListNode(1)
                        carry_over = 0
            return l2


    def addTwoNumbersLazy(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Lazy solution, read two linked lists, add them, create and return a new linked list"""
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        def get_num(l):
            num = ""
            curr = l
            while curr:
                num = str(curr.val) + num
                curr = curr.next
            return int(num)

        num1 = get_num(l1)
        num2 = get_num(l2)

        num = str(num1 + num2)

        head = ListNode()
        curr = head
        for i in range(len(num) - 1, -1, -1):
            curr.next = ListNode(int(num[i]))
            curr = curr.next

        return head.next
