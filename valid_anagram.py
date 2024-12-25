# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        
        return collections.Counter(s) == collections.Counter(t)


assert Solution().isAnagram('anagram', 'nagaram')
assert not Solution().isAnagram('car', 'rat')
assert not Solution().isAnagram('ab', 'a')
