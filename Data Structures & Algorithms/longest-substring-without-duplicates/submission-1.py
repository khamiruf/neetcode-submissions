class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxLen = 0
        # init a dic with char[l]
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            if s[r] not in char_set:
                char_set.add(s[r])
                length = r - l + 1
                maxLen = max(maxLen, length)
            
                    
        return maxLen
