class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # check end of n-1 interval, and start of n interval
        # if end of n-1 <= start of n, merge it
        # append the result to `output`
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for i in range(len(intervals)-1):
            start = intervals[i+1][0]
            end = output[-1][-1]
            if start <= end:
                new_end = max(intervals[i+1][-1],end)
                output[-1][-1] = new_end
            else:
                output.append(intervals[i+1])

        return output