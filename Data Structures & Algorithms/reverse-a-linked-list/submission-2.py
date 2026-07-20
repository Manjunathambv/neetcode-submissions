# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseListHelper(self, head, previous):
        if head is None:
            return previous

        next_node = head.next

        head.next = previous

        return self.reverseListHelper(next_node, head)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return
        previous = None
        return self.reverseListHelper(head, previous)
