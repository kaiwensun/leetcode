from collections import Counter, defaultdict
class Solution(object):

    class LoopDetected(Exception):
        pass

    def sortItems(self, n, m, item2group, item2befores):
        """
        :type n: int
        :type m: int
        :type item2group: List[int]
        :type item2befores: List[List[int]]
        :rtype: List[int]
        """

        def topological_sort_graph(graph, collector=[]):
            status = defaultdict(int)  # 0: not visited; 1: visiting; 2: visited
            def dfs(node):
                if status[node] == 0:
                    status[node] += 1
                    for prereq in graph[node]:
                        dfs(prereq)
                    collector.append(node)
                    status[node] += 1
                elif status[node] == 1:
                    raise Solution.LoopDetected("%d is being visited" % node)
            for node in (graph.keys() if isinstance(graph, dict) else xrange(len(graph))):
                if status[node] == 0:
                    dfs(node)

        singleton = 0
        for item in xrange(n):
            if item2group[item] == -1:
                item2group[item] = m + singleton
                singleton += 1
        m += singleton
        groups_external = [set() for _ in xrange(m)]
        groups_internal = [defaultdict(list) for _ in xrange(m)]
        for item, item2before in enumerate(item2befores):
            for before in item2before:
                item_group = item2group[item]
                before_group = item2group[before]
                if item_group == before_group:
                    groups_internal[item_group][item].append(before)
                else:
                    groups_external[item_group].add(before_group)
        for item, group in enumerate(item2group):
            groups_internal[group][item]

        try:
            sorted_groups_external = []
            topological_sort_graph(groups_external, sorted_groups_external)
            sorted_groups_internal = []
            for group in sorted_groups_external:
                topological_sort_graph(groups_internal[group], sorted_groups_internal)
            return sorted_groups_internal
        except Solution.LoopDetected:
            return []

