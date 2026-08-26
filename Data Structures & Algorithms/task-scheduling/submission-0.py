class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # identical tasks must be separated by at least n CPU cycles --> use queue to keep track
        # use maxHeap to keep track of tasks and schedule the highest freq tasks first
        task_count = {}
        for task in tasks:
            if task in task_count:
                task_count[task] += 1
            else:
                task_count[task] = 1
            
        maxHeap = [-count for count in task_count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time+n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time