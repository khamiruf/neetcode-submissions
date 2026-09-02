class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl_map = {}

        for i,n in enumerate(nums):
            compl = target - n
            if compl in compl_map:
                return [compl_map[compl], i]

            compl_map[n] = i

        return [-1, -1]