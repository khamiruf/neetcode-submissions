class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for x in range(len(temperatures))]
        n = len(temperatures)
        stack = []  # will store indices

        for i in range(n):
            # While current day is warmer than the day at the top of the stack,
            # that top day has found its next warmer temperature at day i.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                res[prev_i] = i - prev_i

            # Current day is now waiting for a warmer future day
            stack.append(i)

        return res