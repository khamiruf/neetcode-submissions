class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        most_water = 0

        while l < r:
            h = min(heights[l], heights[r])
            breadth = r - l
            area = h * breadth
            most_water = max(most_water, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return most_water
