class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_bucket = defaultdict(list)

        for s in strs:
            ch_count = [0 for _ in range(26)]
            for ch in s:
                idx = ord(ch) - ord('a')
                ch_count[idx] += 1
            tup_ch_count = tuple(ch_count)
            char_count_bucket[tup_ch_count].append(s)
        
        return list(char_count_bucket.values())