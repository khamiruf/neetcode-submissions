from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_counts = Counter(s1)
        window_len = len(s1)

        s2_counts = {}
        l = 0
        r = 0

        while r < len(s2) and (r - l + 1) < window_len:
            s2_counts[s2[r]] = s2_counts.get(s2[r], 0) + 1
            r += 1

        while r < len(s2):
            # include s2[r] into the window
            s2_counts[s2[r]] = s2_counts.get(s2[r], 0) + 1

            # now window size is exactly window_len
            if s2_counts == s1_counts:
                return True

            # remove s2[l] from the window before sliding
            s2_counts[s2[l]] -= 1
            if s2_counts[s2[l]] == 0:
                del s2_counts[s2[l]]

            l += 1
            r += 1

        return False
