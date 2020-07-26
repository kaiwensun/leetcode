import functools, collections
class Solution:
    def getProbability(self, balls: List[int]) -> float:
        box_size = sum(balls) // 2
        
        factorial = [1] * (max(balls) + 1 + 100)
        for i in range(1, len(factorial)):
            factorial[i] = factorial[i - 1] * i
            
        def choose(total, select):
            return factorial[total] // (factorial[select] * factorial[total - select])

        def search(color, space_l, space_r, uniq_l, uniq_r):
            cnt_uniq = cnt_total = 0
            if color == len(balls):
                assert(space_l == space_r == 0)
                if uniq_l == uniq_r:
                    return 1, 1
                else:
                    return 0, 1
            for left in range(balls[color] + 1):
                right = balls[color] - left
                if left > space_l or right > space_r:
                    continue
                new_uniq_l = uniq_l + (1 if left else 0)
                new_uniq_r = uniq_r + (1 if right else 0)
                rtn_uniq, rtn_total = search(color + 1, space_l - left, space_r - right, new_uniq_l, new_uniq_r)
                weight = choose(space_l, left) * choose(space_r, right)
                cnt_uniq += rtn_uniq * weight
                cnt_total += rtn_total * weight
            return cnt_uniq, cnt_total
        stats = search(0, box_size, box_size, 0, 0)
        return float(stats[0]) / stats[1]
