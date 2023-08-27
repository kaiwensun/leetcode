class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        prev_step = 1
        step = 2
        dp = {1: list(enumerate(receiver))}
        while step <= k:
            row = []
            for start in range(len(receiver)):
                step1 = dp[prev_step][start]
                step2 = dp[prev_step][step1[1]]
                row.append([step1[0] + step2[0], step2[1]])
            dp[step] = row
            prev_step = step
            step <<= 1

        def calc(node):
            remain_step = k
            res = 0
            while remain_step:
                step = remain_step - (remain_step & (remain_step - 1))
                step_res = dp[step][node]
                res += step_res[0]
                node = step_res[1]
                remain_step -= step
            return res + node

        return max(calc(node) for node in range(len(receiver)))

