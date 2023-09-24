class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def calc(maxHeights):
            res = []
            stack = [[0, 0]]  # [[height, count], ...]
            sm = 0
            for num in maxHeights:
                cur = [num, 1]
                sm += num
                while stack[-1][0] >= cur[0]:
                    tail = stack.pop()
                    sm -= (tail[0] - cur[0]) * tail[1]
                    cur[1] += tail[1]
                stack.append(cur)
                res.append(sm)
            return res
        left = calc(maxHeights)
        right = list(reversed(calc(list(reversed(maxHeights)))))
        return max(left[i] + right[i] - maxHeights[i] for i in range(len(maxHeights)))

