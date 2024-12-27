# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    """Straight foraward solution"""
    def reverseBits(self, n: int) -> int:
        n_binary_representation = f'{n:032b}'

        return int(n_binary_representation[::-1], 2)


class Solution:
    """Classic approach"""
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result


assert Solution().reverseBits(43261596) == 964176192
assert Solution().reverseBits(4294967293) == 3221225471
