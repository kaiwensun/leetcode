class Solution(object):
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        """
        :type flowers: List[int]
        :type newFlowers: int
        :type target: int
        :type full: int
        :type partial: int
        :rtype: int
        """
        flowers = sorted(min(f, target) for f in flowers)
        N = len(flowers)
        if flowers[0] == target:
            return N * full
        flowers.append(float("inf"))
        fill_start = bisect.bisect_left(flowers, target)
        remain_flowers = min(newFlowers, target * N - sum(flowers[:-1]))
        while fill_start > 0 and target - flowers[fill_start - 1] <= remain_flowers:
            fill_start -= 1
            remain_flowers -= target - flowers[fill_start]
        if fill_start == 0:
            return max(N * full, (target - 1) * partial + (N - 1) * full)
        res = flowers[0] * partial + (N - fill_start) * full
        min_cnt = 1
        for min_flower in range(flowers[0] + 1, target):
            while flowers[min_cnt] < min_flower:
                min_cnt += 1
            remain_flowers -= min(min_cnt, fill_start)
            while remain_flowers < 0 and fill_start < N:
                remain_flowers += target - max(flowers[fill_start], min_flower)
                fill_start += 1
            if remain_flowers < 0:
                break
            res = max(res, min_flower * partial + (N - fill_start) * full)
        return res

