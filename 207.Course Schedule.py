class Solution(object):
    def canFinish(self, n, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        next_courses = [set() for _ in xrange(n)]
        for preq in prerequisites:
            next_courses[preq[1]].add(preq[0])  
        status = [0] * n  # 0: not visited; 1 visiting; 2 visited
        for course in xrange(n):
            if not self.dfs(status, course, next_courses):
                return False
        return True

    def dfs(self, status, visiting, next_courses):
        if status[visiting] == 2:
            return True
        if status[visiting] == 1:
            return False
        status[visiting] += 1
        for next_course in next_courses[visiting]:
            if not self.dfs(status, next_course, next_courses):
                return False
        status[visiting] += 1
        return True
