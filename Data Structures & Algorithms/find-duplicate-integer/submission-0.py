class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # exactly one repeated int
        # O(1) space
        # [1..n] -- n = len(nums)
        unique_nums = set()
        for n in nums:
            if n in unique_nums:
                return n
            
            unique_nums.add(n)
        
        return -1