class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1

        maxL = height[0]
        maxR = height[-1]
        water = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(height[l], maxL)
                water += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                water += maxR - height[r]
        
        return water
            