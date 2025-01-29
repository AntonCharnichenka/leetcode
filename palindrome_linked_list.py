# https://leetcode.com/problems/palindrome-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        values = [head.val]

        while head.next:
            head = head.next
            values.append(head.val)

        return values == values[::-1]


assert (
    Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1, None)))))
    is True
)
assert Solution().isPalindrome(ListNode(1, ListNode(2, None))) is False
