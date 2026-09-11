class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s and t:
            return False
        if s and not t:
            return False
            
        ch_count = [0] * 26
        
        for ch in s:
            ch_count[ord(ch) - ord('a')] += 1

        for tch in t:
            ch_count[ord(tch) - ord('a')] -= 1
        
        return True if all(x == 0 for x in ch_count) else False