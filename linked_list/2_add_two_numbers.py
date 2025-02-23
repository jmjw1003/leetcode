# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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