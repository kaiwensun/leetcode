import fractions
from collections import defaultdict

class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        stacks = defaultdict(list)
        ans = [-1] * len(nums)

        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        coprimes = defaultdict(list)
        uniqs = list(set(nums))
        for i in xrange(len(uniqs)):
            for j in xrange(i + 1, len(uniqs)):
                if fractions.gcd(uniqs[i], uniqs[j]) == 1:
                    coprimes[uniqs[i]].append(uniqs[j])
                    coprimes[uniqs[j]].append(uniqs[i])
        coprimes[1].append(1)
        stacks = defaultdict(list)

        def dfs(node, parent, depth):
            num = nums[node]
            coprime_node = -1
            coprime_depth = -1
            for coprime in coprimes[num]:
                stack = stacks[coprime]
                if stack and stack[-1][1] > coprime_depth:
                    coprime_node, coprime_depth = stack[-1]
            ans[node] = coprime_node
            stacks[num].append((node, depth))
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node, depth + 1)
            stacks[num].pop()

        dfs(0, None, 0)
        return ans

