class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for _ in range(len(nums))]

        # use prefix = 1
        # prefix * nums[i] = output[i]
        # postfix = 1
        # traverse in reverse, postfix * nums[i] *= output[i]

        pre = 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]

        post = 1
        for x in range(len(nums)-1, -1, -1):
            output[x] *= post
            post *= nums[x]

        return output