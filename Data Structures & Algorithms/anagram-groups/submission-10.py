class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_counts = defaultdict(list)

        for strng in strs:
            char_count = [0 for _ in range(26)]

            for c in strng:
                idx = ord(c) - ord('a')
                char_count[idx] += 1
            
            tup_char_count = tuple(char_count)
            str_counts[tup_char_count].append(strng)
        
        return list(str_counts.values())