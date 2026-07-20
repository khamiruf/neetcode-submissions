class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k < 1 or not nums:
            return [-1]
        
        count_nums = {}
        for n in nums:
            count_nums[n] = count_nums.get(n, 0) + 1
        
        count_bucket = [[] for _ in range(len(nums)+1)]
        for key,v in count_nums.items():
            count_bucket[v].append(key)

        res=[]
        for i in range(len(count_bucket)-1, 0, -1):
            if count_bucket[i]:
                for ele in count_bucket[i]:
                    if len(res) == k:
                        break
                    res.append(ele)
        return res
        
