class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in compl:
                return [compl[comp], i]
            else:
                compl[n] = i
        
        return [-1,-1]