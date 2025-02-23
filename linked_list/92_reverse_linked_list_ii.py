from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case
        if left == right:
            return head

        # Head could be moved so can adding a dummy node in front
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        # Get to part we are reversing
        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        
        # Save prior node so we can join to end of reverse section
        l = prev

        # Reverse section
        for _ in range(right + 1 - left):
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        # Update pointers
        r = l.next
        r.next = next_
        l.next = prev

        return dummy.next


def main():
    """Testing."""
    head = ListNode(1)
    curr = head
    for i in range(2, 6):
        curr.next = ListNode(i)
        curr = curr.next

    s = Solution()

    res = s.reverseBetween(head, 2, 4)

    curr = res

    while curr:
        print(f"( {curr.val} ) -> ", end="")
        curr = curr.next
    print("")


if __name__ == "__main__":
    main()
