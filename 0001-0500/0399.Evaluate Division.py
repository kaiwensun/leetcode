class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        inf = float('Inf')
        var_ind_map = {}
        i = 0
        for equation in equations:
            for variable in equation:
                if variable not in var_ind_map:
                    var_ind_map[variable] = i
                    i += 1
        var_cnt = len(var_ind_map)
        for i in xrange(len(queries)):
            query = queries[i]
            if query[0] not in var_ind_map or query[1] not in var_ind_map:
                queries[i] = None
            elif query[0] == query[1]:
                queries[i] = (-1, -1)
            else:
                queries[i] = (var_ind_map[query[0]], var_ind_map[query[1]])

        results = [-1.0] * len(queries)
        
        grid = [[inf] * i for i in xrange(var_cnt)]
        for i in xrange(len(equations)):
            equation = equations[i]
            ind1, ind2 = var_ind_map[equation[0]], var_ind_map[equation[1]]
            if ind1 > ind2:
                grid[ind1][ind2] = values[i]
            elif ind1 < ind2:
                grid[ind2][ind1] = 1/values[i]

        query_ind_map = {}
        for i in xrange(len(queries)):
            query = queries[i]
            if query == None:
                results[i] = -1.0
            elif query[0] == query[1]:
                results[i] = 1.0
            elif query[0] < query[1]:
                if grid[query[1]][query[0]] != inf:
                    results[i] = 1 / grid[query[1]][query[0]]
                else:
                    q = (query[1], query[0])
                    value = -i -1
                    if q in query_ind_map:
                        query_ind_map[q].add(value)
                    else:
                        query_ind_map[q] = set([value])
            else:
                if grid[query[0]][query[1]] != inf:
                    results[i] = grid[query[0]][query[1]]
                else:
                    q = (query[0], query[1])
                    value = i
                    if q in query_ind_map:
                        query_ind_map[q].add(value)
                    else:
                        query_ind_map[q] = set([value])
        
        if query_ind_map:
            for k in xrange(var_cnt):
                if query_ind_map:
                    for i in xrange(var_cnt):
                        if query_ind_map:
                            for j in xrange(var_cnt):
                                if i == j:
                                    continue
                                if grid[max(i, j)][min(i, j)] != inf:
                                    continue
                                if not query_ind_map:
                                    break
                                subpath1 = 1 if i == k else grid[max(k, i)][min(i, k)]
                                if subpath1 == inf:
                                    continue
                                if k < i:
                                    subpath1 = 1 / subpath1
                                subpath2 = 1 if j == k else grid[max(j, k)][min(k, j)]
                                if subpath2 == inf:
                                    continue
                                if j < k:
                                    subpath2 = 1 / subpath2
                                grid[max(j, i)][min(i, j)] = subpath1 * subpath2 if j > i else 1 / subpath1 / subpath2
                                q = (max(j, i), min(i, j))
                                if q in query_ind_map:
                                    indexes = query_ind_map[q]
                                    for index in indexes:
                                        if index >= 0:
                                            results[index] = grid[q[0]][q[1]]
                                        else:
                                            results[- index - 1] = 1 / grid[q[0]][q[1]]
                                    del query_ind_map[q]
        return results

