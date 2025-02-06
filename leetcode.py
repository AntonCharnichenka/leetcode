# # import random
# #
# #
# # class Solution:
# #
# #     def twoSum(self, nums: list[int], target: int) -> list[int]:
# #         nums_len = len(nums)
# #         print('nums_len', nums_len)
# #         a = b = None
# #
# #         while True:
# #             i = random.randint(0, nums_len - 1)
# #             print('i', i)
# #             x = nums[i]
# #             print('x', x)
# #             y = random.choice(nums[0:i] + nums[i:])
# #             print('y', y)
# #             print('---')
# #             if x + y == target:
# #
# #                 a = nums.index[x]
# #                 b = nums.index[y]
# #                 break
# #
# #         return [a, b]
# #
# #
# # Solution().twoSum([2, 7, 11, 15], 9)
#
#
# # import random
# #
# # class Solution:
# #     def twoSum(self, nums: list[int], target: int) -> list[int]:
# #         for ix, x in enumerate(nums):
# #             for iy, y in enumerate(nums):
# #                 if ix != iy and (x + y == target):
# #                     return [nums.index(ix), nums.index(y)]
# #
# #
# # print(Solution().twoSum([3,3], 6))
#
#
# # class Solution:
# #     def isPowerOfThree(self, n: int) -> bool:
# #         import math
# #         if int(math.log(n, 3)) == 3:
# #             return True
# #
# #         return False
# #
# #
# # print(Solution().isPowerOfThree(27))
#
#
# # class Solution:
# #     def romanToInt(self, s: str) -> int:
# #         map = (
# #             ('M', 1000),
# #             ('D', 500),
# #             ('CM', 900),
# #             ('CD', 400),
# #             ('C', 100),
# #             ('L', 50),
# #             ('XC', 90),
# #             ('XL', 40),
# #             ('X', 10),
# #             ('V', 5),
# #             ('IV', 4),
# #             ('I', 1),
# #         )
# #
# #         sum = 0
# #         while s:
# #             for ch, v in map:
# #                 if s.startswith(ch):
# #                     sum += v
# #                     s = s[len(ch):]
# #                     break
# #
# #         return sum
# #
# #
# # print(Solution().romanToInt('XXVII'))
#
# # class Solution:
# #     def longestCommonPrefix(self, strs: list[str]) -> str:
# #         result = ''
# #         for index in range(len(base := min(strs, key=len))):
# #             if len(set(s[index] for s in strs)) == 1:
# #                 result += base[index]
# #             else:
# #                 break
# #
# #         return result
# #
# #
# # print(Solution().longestCommonPrefix(["cir","car"]))
#
#
# # class Solution:
# #     def isValid(self, s: str) -> bool:
# #         if len(s) % 2 != 0:
# #             return False
# #
# #         open_brackets = ['(', '[', '{']
# #         close_brackets = [')', ']', '}']
# #
# #         stack = []
# #         for ch in s:
# #             if ch in open_brackets:
# #                 stack.append(ch)
# #             elif ch in close_brackets:
# #                 if open_brackets.index(stack[-1]) != close_brackets.index(ch):
# #                     return False
# #                 else:
# #                     stack.pop(-1)
# #
# #         return True
# #
# #
# # print(Solution().isValid('{[]}'))
#
# # class ListNode:
# #     def __init__(self, val: int = 0, next: 'ListNode' | None = None):
# #         self.val = val
# #         self.next = next
#
# #     def __repr__(self):
# #         return str(self.val)
# #
# #
# # ln2 = ListNode(2, None)
# # ln1 = ListNode(1, ln2)
# #
# # l = [ln2, ln1]
# #
# #
# # class Solution:
# #     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# #         # result = []
# #         # list11 = []
# #         #
# #         # for i, ln in enumerate(reversed(sorted(list1 + list2, key=lambda ln: ln.val))):
# #         #     if len(result) == 0:
# #         #         ln.next = None
# #         #     else:
# #         #         ln.next = result[-1]
# #         #
# #         #     result.insert(0, ln)
# #         #
# #         # return result
# #
# #         result = []
# #
# #
# # print(Solution().mergeTwoLists())
#
#
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# #
# #     def __repr__(self):
# #         return f'val={self.val} next_val={self.next.val}'
# #
# #
# # ln14 = ListNode(4)
# # ln12 = ListNode(2, ln14)
# # ln11 = ListNode(1, ln12)
# #
# #
# # ln24 = ListNode(4)
# # ln22 = ListNode(3, ln24)
# # ln21 = ListNode(1, ln22)
# #
# #
# # from typing import Optional
#
# # class Solution:
# #     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# #         list1_values = []
# #         while True:
# #             if list1.next is not None:
# #                 list1_values.append(list1.val)
# #                 list1 = list1.next
# #             else:
# #                 list1_values.append(list1.val)
# #                 break
# #
# #         list2_values = []
# #         while True:
# #             if list2.next is not None:
# #                 list2_values.append(list2.val)
# #                 list2 = list2.next
# #             else:
# #                 list2_values.append(list2.val)
# #                 break
# #
# #         unlinked_nodes = [ListNode(v) for v in sorted(list1_values + list2_values)]
# #         for i in range(len(unlinked_nodes) - 1):
# #             unlinked_nodes[i].next = unlinked_nodes[i + 1]
# #
# #         return unlinked_nodes[0]
#
#
# # class Solution:
# #     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# #         if list1 is None:
# #             return list2
# #
# #         if list2 is None:
# #             return list1
# #
# #         if list1 is None and list2 is None:
# #             return None
# #
# #         cursor = dummy = ListNode()
# #         while list1 and list2:
# #             if list1.val < list2.val:
# #                 cursor.next = list1
# #                 list1 = list1.next
# #                 cursor = list1
# #             else:
# #                 cursor.next = list2
# #                 list2 = list2.next
# #                 cursor = list2
# #
# #         # while list1 and list2:
# #         #     if list1.val < list2.val:
# #         #         cursor.next = list1
# #         #         list1, cursor = list1.next, list1
# #         #     else:
# #         #         cursor.next = list2
# #         #         list2, cursor = list2.next, list2
# #
# #         return dummy.next
# #
# #
# # print(Solution().mergeTwoLists(ln11, ln21))
#
#
# # class Solution:
# #     def removeDuplicates(self, nums: list[int]) -> int:
# #         if len(nums) == 1:
# #             return 1
# #
# #         seen = {nums[0], }
# #         i = 1
# #         while True:
# #             if nums[i] not in seen:
# #                 seen.add(nums[i])
# #                 i += 1
# #             else:
# #                 nums.pop(i)yfc
# #
# #             if i == len(nums):
# #                 break
# #
# #         return len(nums)
# #
# #
# # print(Solution().removeDuplicates([1,1]))
#
#
# # class Solution:
# #     def strStr(self, haystack: str, needle: str) -> int:
# #         if not needle in haystack:
# #             return -1
# #
# #         needle_len = len(needle)
# #
# #         for i in range(len(haystack) - needle_len + 1):
# #             if needle == haystack[i: i + needle_len]:
# #                 return i
# #
# #         return -1
# #
# #
# # print(Solution().strStr('funnandfunny', 'funny'))
#
#
# # class Solution:
# #     def plusOne(self, digits: list[int]) -> list[int]:
# #         s = int(''.join(str(n) for n in digits))
# #         return [int(ch) for ch in str(s+1)]
# #
# # print(Solution().plusOne([5,9]))
#
#
# # class Solution:
# #     def mySqrt(self, x: int) -> int:
# #         if x == 0:
# #             return 0
# #         if x == 1:
# #             return 1
# #
# #         i = 0; j = x
# #
# #         while True:
# #             guess = (j + i) / 2
# #             square = guess * guess
# #             if abs(square - x) < 0.1:
# #                 return int(round(guess, 2))
# #             elif square > x:
# #                 j = guess
# #             elif square < x:
# #                 i = guess
# #
# #
# #
# #
# # print(Solution().mySqrt(2))
#
# # class Solution:
# #     def moveZeroes(self, nums: List[int]) -> None:
# #         """
# #         Do not return anything, modify nums in-place instead.
# #
# #         """
# #         zeros_count = 0
# #         l = []
# #         for el in nums:
# #             if el == 0:
# #                 zeros_count += 1
# #             else:
# #                 l.append(el)
# #
# #         l.extend([0] * zeros_count)
# #
# #         nums[:] = l
# #
#
# # class Solution:
# #     def climbStairs(self, n: int) -> int:
# #         if n == 1:
# #             return 1
# #         if n == 2:
# #             return 2
# #
# #         d = [0] * n
# #         d[0] = 1
# #         d[1] = 2
# #         for i in range(2, len(d)):
# #             d[i] = d[i - 1] + d[i - 2]
# #
# #         return d[n-1]
# #
# # print(Solution().climbStairs(3))
#
# # class Solution:
# #     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
# #         """
# #         Do not return anything, modify nums1 in-place instead.
# #         """
# #         if n == 0:
# #             return nums1
# #
# #         if m == 0:
# #             nums1[:] = nums2
# #             return
# #
# #         while True:
# #             if nums1[-1] == 0:
# #                 nums1.pop(-1)
# #             else:
# #                 break
# #
# #         r = []
# #         while nums1 or nums2:
# #             if not nums1:
# #                 r.extend(nums2)
# #                 break
# #             elif not nums2:
# #                 r.extend(nums1)
# #                 break
# #             elif nums1[0] < nums2[0]:
# #                 r.append(num1.pop(0))
# #             else:
# #                 r.append(nums2.pop(0))
# #
# #         nums1[:] = r
# #
# # nums1 = [0]
# #
# # Solution().merge(nums1, 0, [1], 1)
# #
# # print(nums1)
# #
#
# # class Solution:
# #     def missingNumber(self, nums: list[int]) -> int:
# #         # a = range(len(nums) + 1)
# #         # import itertools
# #
# #         # d = itertools.zip_longest(a, sorted(nums))
# #         # for x, y in d:
# #         #     if y != x:
# #         #         return x
# #         if len(nums) == 1:
# #             return 1
# #
# #         a = sorted(nums)
# #         curr = a[0]
# #         for i in range(1, len(nums)):
# #             if a[i] - curr == 1:
# #                 curr = a[i]
# #             else:
# #                 return a[i] - 1
# #
# #         return len(nums)
# #
# #
# # print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
# #
# # class Solution:
# #     def reverseString(self, s: list[str]) -> None:
# #         """
# #         Do not return anything, modify s in-place instead.
# #         """
# #         i = 0
# #         l = len(s)
# #         while i <= l - 1:
# #             s.insert(i, s.pop())
# #             i += 1
# #
# # i = ["h","e","l","l","o"]
# # Solution().reverseString(i)
# # print(i)
#
# # class Solution:
# #     def firstUniqChar(self, s: str) -> int:
# #         m = {}
# #         for ch in s:
# #             if m.get(ch) is None:
# #                 m[ch] = s.count(ch)
# #             if m[ch] == 1:
# #                 return s.index(ch)
# #
# #         return -1
#
# # print(Solution().firstUniqChar(a))
#
#
# # class Solution:
# #     def containsDuplicate(self, nums: List[int]) -> bool:
# #         seen = set()
# #
# #         for num in nums:
# #             if num not in seen:
# #                 seen.add(num)
# #                 continue
# #
# #             return True
# #
# #         return False
#
# # class Solution:
# #     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
# #         from collections import Counter
# #         c1 = Counter(nums1)
# #         c2 = Counter(nums2)
# #
# #         result = []
# #         for k in c1:
# #             if c2.get(k):
# #                 result.extend([k] * min(c1[k], c2[k]))
# #
# #         return result
# #
# #
# # print(Solution().intersect([1,2,2,1], [2,2]))
#
#
# class Solution:
#     @staticmethod
#     def isHappy(n: int) -> bool:
#         if n == 1:
#             return True
#
#         def check(parts_: list[int]) -> bool:
#             if sum(x ** 2 for x in parts_) == 1:
#                 return True
#
#             return False
#
#         parts = [int(p) for p in str(n)]
#
#         import itertools
#         for i in itertools.count(1000000000):
#             if check(parts):
#                 return True
#
#             parts = [int(p) for p in str(int(sum(parts)))]
#
#         return False
#
#
# print(Solution().isHappy(2))
#
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         hset = set()
#         while n != 1:
#             if n in hset:
#                 return False
#             hset.add(n)
#             n = sum([int(i) ** 2 for i in str(n)])
#         else:
#             return True
#
#
# print(Solution().isHappy(2))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next_):
        self.val = x
        self.next = next_

    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    @staticmethod
    def hasCycle(head: ListNode | None) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True

        return False


test_head1 = ListNode("1", ListNode("2", ListNode("3", None)))

print(Solution().hasCycle(test_head1))
