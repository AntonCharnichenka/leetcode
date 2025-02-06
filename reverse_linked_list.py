from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val: int = 0, next_: Optional["ListNode"] = None):
        self.val = val
        self.next = next_

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    """Straigh forward solution"""

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        nodes: list[ListNode] = []
        node = head
        nodes.append(node)
        while True:
            if node.next:
                nodes.append(node.next)
                node = node.next
            else:
                break

        reversed_nodes: list[ListNode] = list(reversed(nodes))
        for i, node in enumerate(reversed(nodes)):
            if i == len(reversed_nodes) - 1:
                node.next = None
                break

            node.next = reversed_nodes[i + 1]

        return reversed_nodes[0]


class Solution:
    """2 pointers"""

    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev

            # move pointers
            prev = curr
            curr = next_node

        return prev


NODE = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))


print(Solution().reverseList(NODE))
