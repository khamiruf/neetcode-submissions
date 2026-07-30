class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set()
        max_len = 0

        for n in nums:
            if n not in unique_nums:
                unique_nums.add(n)
        
        for i in range(len(nums)):
            if nums[i]-1 not in unique_nums:
                # this is the start of the seq
                x = nums[i]
                seq_len = 0
                while x in unique_nums:
                    seq_len += 1
                    x += 1
                max_len = max(max_len, seq_len)
            else:
                continue
        
        return max_len