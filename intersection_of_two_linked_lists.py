# https://leetcode.com/problems/intersection-of-two-linked-lists/description/


# Definition for singly-linked list
class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        flattened_list_a = [headA]
        pointer_a = headA
        while pointer_a.next:
            pointer_a = pointer_a.next
            flattened_list_a.append(pointer_a)

        flattened_list_b = [headB]
        pointer_b = headB
        while pointer_b.next:
            pointer_b = pointer_b.next
            flattened_list_b.append(pointer_b)

        intersect_node = None
        for node_a, node_b in zip(
            reversed(flattened_list_a), reversed(flattened_list_b)
        ):
            if node_a is node_b:
                intersect_node = node_a
            else:
                break

        return intersect_node


# NODE = ListNode(8, ListNode(4, ListNode(5, None)))

# assert (
#     Solution()
#     .getIntersectionNode(
#         ListNode(4, ListNode(1, NODE)),
#         ListNode(5, ListNode(6, ListNode(1, NODE))),
#     )
#     .val
#     == NODE.val
# )


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        pointer_a, pointer_b = headA, headB
        while pointer_a is not pointer_b:
            pointer_a = pointer_a.next if pointer_a is not None else headB
            pointer_b = pointer_b.next if pointer_b is not None else headA

        return pointer_a


NODE = ListNode(8, ListNode(4, ListNode(5, None)))

assert (
    Solution2()
    .getIntersectionNode(
        ListNode(4, ListNode(1, NODE)),
        ListNode(5, ListNode(6, ListNode(1, NODE))),
    )
    .val
    == NODE.val
)

assert (
    Solution2().getIntersectionNode(
        ListNode(2, ListNode(6, ListNode(4, None))),
        ListNode(1, ListNode(5, None)),
    )
    is None
)
