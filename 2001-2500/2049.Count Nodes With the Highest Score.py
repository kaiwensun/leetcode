from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        children = defaultdict(list)
        for child, parent in enumerate(parents):
            children[parent].append(child)

        factors = defaultdict(list)

        def calc_subtree_size(node):
            for child in children[node]:
                factors[node].append(calc_subtree_size(child))
            return sum(factors[node]) + 1
        scores = [None] * N
        def dfs(node, top_size):
            prod = max(1, top_size)
            for factor in factors[node]:
                prod *= factor
            scores[node] = prod
            sm = sum(factors[node])
            for i, child in enumerate(children[node]):
                dfs(child, top_size + 1 + sm - factors[node][i])
        calc_subtree_size(0)
        dfs(0, 0)
        mx = max(scores)
        return scores.count(mx)

