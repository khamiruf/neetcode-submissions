class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the damn letters in a bucket
        # tuple : list of words
        anag_map = {}

        for s in strs:
            new_bucket = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                new_bucket[idx] += 1
            
            tup_buck = tuple(new_bucket)
            if tup_buck in anag_map:
                anag_map[tup_buck].append(s)
            else:
                anag_map[tup_buck] = [s]
        
        return list(anag_map.values())