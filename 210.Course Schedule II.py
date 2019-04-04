class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.prev_courses = [set() for _ in xrange(numCourses)]
        self.learned_courses = set()
        self.want_to_learn = set()
        self.schedule = []
        for preq in prerequisites:
            self.prev_courses[preq[0]].add(preq[1])
        for course in xrange(numCourses):
            if not self.dfs_learn(course):
                return []
        return self.schedule
        
    def dfs_learn(self, course):
        if course in self.learned_courses:
            return True
        if course in self.want_to_learn:
            return False
        self.want_to_learn.add(course)
        for preq in self.prev_courses[course]:
            if not self.dfs_learn(preq):
                return False
        self.want_to_learn.remove(course)
        self.learned_courses.add(course)
        self.schedule.append(course)
        return True
