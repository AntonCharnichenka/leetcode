# https://leetcode.com/problems/valid-palindrome/description/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join(ch.lower() for ch in s if ch.isalnum())

        return filtered_s == filtered_s[::-1]


assert Solution().isPalindrome("A man, a plan, a canal: Panama")
assert not Solution().isPalindrome("race a car")
assert Solution().isPalindrome(" ")
