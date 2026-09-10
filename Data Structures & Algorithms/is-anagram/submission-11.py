class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (s and not t) or (t and not s):
            return False
        if len(s) != len(t):
            return False
        
        ch_count = {}
        for ch in s:
            ch_count[ch] = 1 + ch_count.get(ch, 0)
        
        for cha in t:
            if cha not in ch_count:
                return False
            else:
                ch_count[cha] -= 1
        
        if not all(val == 0 for val in ch_count.values()):
            return False
        
        return True