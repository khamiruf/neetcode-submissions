class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # store index, height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                last_i, last_h = stack.pop()
                new_area = last_h * (i - last_i)
                max_area = max(max_area, new_area)
                start = last_i
            
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area