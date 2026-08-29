class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # start each key with an empty list first
        # then use prerequisites to map each course to prereq list
        preMap = {
            i: [] for i in range(numCourses)
        }
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set() # track the courses along the curr DFS path
        def dfs(crs):
            if crs in visitSet:
                return False
            if not preMap[crs]:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): 
                    return False
            visitSet.remove(crs)
            preMap[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True