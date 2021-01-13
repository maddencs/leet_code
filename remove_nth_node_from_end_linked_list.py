# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        current_node_idx = 0
        before_nth_node = head
        nth_node = head
        current = head
        while current:
            current = current.next
            if current_node_idx >= n:
                before_nth_node = nth_node
                nth_node = nth_node.next

            current_node_idx += 1

        before_nth_node.next = nth_node.next
        if current_node_idx <= n:
            return head.next

        return head
