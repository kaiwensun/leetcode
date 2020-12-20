from collections import defaultdict
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        answer = [None] * len(quiet)
        graph = defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        def dfs(person):
            if answer[person] is None:
                quietest_person = person
                min_quietness = quiet[person]
                for neighbor in graph[person]:
                    p = dfs(neighbor)
                    if quiet[p] < min_quietness:
                        min_quietness = quiet[p]
                        quietest_person = p
                answer[person] = quietest_person
            return answer[person]
        for person in xrange(len(quiet)):
            dfs(person)
        return answer

