class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] # convert to negative to emulate maxHeap
        heapq.heapify(stones) # O (n)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
                
        return -1* stones[0] if stones else 0
