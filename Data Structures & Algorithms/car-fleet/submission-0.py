class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # (target - position) / speed 
        cars = list(zip(position, speed))
        cars.sort(reverse=True, key=lambda x: x[0])

        stack = []
        for p, s in cars:
            time_at_dest = (target - p)/ s
            stack.append(time_at_dest)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)