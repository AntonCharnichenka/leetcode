class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string

        m: dict[str, int] = {
            e: i for i, e in enumerate(string.ascii_uppercase, start=1)
        }

        if len(columnTitle) == 1:
            return m[columnTitle]

        return sum(len(m) ** i * m[ch] for i, ch in enumerate(columnTitle[::-1]))


assert Solution().titleToNumber("A") == 1
assert Solution().titleToNumber("AB") == 28
assert Solution().titleToNumber("ZY") == 701
