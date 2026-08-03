class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0 for x in range(len(temperatures))]

        for i in range(len(temperatures)):
            if not stack:
                stack.append((i, temperatures[i])) # maybe need to append the index
            else:
                cur_temp = temperatures[i]
                while cur_temp > stack[-1][-1]:
                    index, _ = stack.pop()
                    out[index] = i-index
                    if not stack:
                        break
                stack.append((i, temperatures[i]))
        
        return out