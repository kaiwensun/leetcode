from collections import Counter
class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # (ball count, number of colors that have such count)
        stack = map(list, Counter(inventory).items())
        stack.append([0, 0])
        stack.sort()
        res = 0
        while orders:
            ball_cnt, color_cnt = stack.pop()
            if (ball_cnt - stack[-1][0]) * color_cnt <= orders:
                new_ball_cnt = stack[-1][0]
                stack[-1][1] += color_cnt
                res += (new_ball_cnt + 1 + ball_cnt) * (ball_cnt - new_ball_cnt) // 2 * color_cnt
                res %= MOD
                orders -= (ball_cnt - new_ball_cnt) * color_cnt
            else:
                each_color_take = orders // color_cnt
                new_ball_cnt = ball_cnt - each_color_take
                res += (ball_cnt - each_color_take + 1 + ball_cnt) * each_color_take // 2 * color_cnt
                orders -= (ball_cnt - new_ball_cnt) * color_cnt
                res += new_ball_cnt * orders
                orders = 0
                res %= MOD
        return res

