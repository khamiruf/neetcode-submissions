class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        for pre, course in prerequisites:
            prereq_map[course].append(pre)
        
        # print(prereq_map)

        visit = set()
        def dfs(course):
            if course in visit:
                return False
            if not prereq_map[course]:
                return True
            
            visit.add(course)
            for pre in prereq_map[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            prereq_map[course] = []

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True