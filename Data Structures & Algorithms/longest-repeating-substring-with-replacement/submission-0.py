class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l=0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            window_len = r-l + 1
            while window_len - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
                window_len = r-l + 1

            res = max(res, window_len)

        return res