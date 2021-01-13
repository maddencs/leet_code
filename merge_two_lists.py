# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        node_1 = l1
        node_2 = l2
        current_tail = None
        head = None
        while node_1 or node_2:
            if node_1:
                if not node_2 or node_1.val <= node_2.val:
                    if head is None:
                        head = node_1
                        current_tail = node_1
                    else:
                        current_tail.next = node_1
                        current_tail = node_1
                    node_1 = node_1.next
            if node_2:
                if not node_1 or node_2.val <= node_1.val:
                    if head is None:
                        head = node_2
                        current_tail = node_2
                    else:
                        current_tail.next = node_2
                        current_tail = node_2
                    node_2 = node_2.next
        return head
