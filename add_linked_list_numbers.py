class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum_list_head = None
        sum_list_tail = None
        current1 = l1
        current2 = l2
        carry = 0
        while current1 or current2:
            left_val = current1.val if current1 else 0
            right_val = current2.val if current2 else 0
            current_sum = left_val + right_val + carry
            remainder = current_sum % 10
            carry = 1 if current_sum >= 10 else 0
            if self._is_last_digit(current1, current2) and current_sum >= 10:
                last_digit = ListNode(int(current_sum / 10))
                sum_node = ListNode(remainder)
                sum_node.next = last_digit
            else:
                sum_node = ListNode(remainder)
            if sum_list_head is None:
                sum_list_head = sum_node
            if sum_list_tail is not None:
                sum_list_tail.next = sum_node
            sum_list_tail = sum_node
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None

        return sum_list_head

    def _is_last_digit(self, current1, current2):
        if current1 and not current1.next and not current2:
            return True
        if current2 and not current2.next and not current1:
            return True
        if current1 and current2 and not current1.next and not current2.next:
            return True

        return False


l1 = None
l1_tail = None
for i in [9,9,9,9,9,9,9]:
    node = ListNode(i)
    if not l1:
        l1 = node
        l1_tail = node
    else:
        l1_tail.next = node
        l1_tail = node


l2 = None
l2_tail = None
for i in [9,9,9,9]:
    node = ListNode(i)
    if not l2:
        l2 = node
        l2_tail = node
    else:
        l2_tail.next = node
        l2_tail = node


sum = Solution().addTwoNumbers(l1, l2)

current = sum
while current:
    print(current.val)
    current = current.next

