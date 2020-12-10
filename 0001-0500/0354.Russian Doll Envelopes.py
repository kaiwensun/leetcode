import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda env : (env[0], -env[1]))
        inc_stack = [float("-inf")]
        seq_sizes = [0]
        for i, env in enumerate(envelopes):
            posi = bisect.bisect_left(inc_stack, env[1])
            if len(inc_stack) == posi:
                inc_stack.append(env[1])
                seq_sizes.append(seq_sizes[-1] + 1)
            else:
                inc_stack[posi] = env[1]
                seq_sizes[posi] = seq_sizes[posi - 1] + 1
        return max(seq_sizes)

