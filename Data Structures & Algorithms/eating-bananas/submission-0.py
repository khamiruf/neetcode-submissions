class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = min int to eat all bananas within h hours
        # h = number of hours to eat all the bananas
        # 1..max(piles)
        l = 1
        r = max(piles) # O(n)
        res = r

        if len(piles) > h:
            return -1
        
        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res


        
