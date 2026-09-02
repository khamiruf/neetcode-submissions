class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        
        char_counts = defaultdict(list)
        for s in strs:
            char_count = [0 for _ in range(26)]
            for ch in s:
                index = ord(ch) - ord('a')
                char_count[index] += 1
            tuple_char_count = tuple(char_count)
            char_counts[tuple_char_count].append(s)
        
        for _, v in char_counts.items():
            res.append(v)
        
        return res