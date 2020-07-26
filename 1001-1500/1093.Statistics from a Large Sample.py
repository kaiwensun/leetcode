class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        LEN = len(count)
        mn = mx = -1
        for i in xrange(LEN):
            if count[i]:
                mx = i
                if mn == -1:
                    mn = i
        cnt = sum(count)
        mean = sum(i * count[i] for i in xrange(LEN)) / float(cnt)
        acc = 0
        for num, c in enumerate(count):
            acc += c
            if cnt % 2 == 1:
                if acc >= (cnt + 1) / 2:
                    median = num
                    break
            else:
                if acc >= cnt / 2:
                    if acc > cnt / 2:
                        median = num
                    else:
                        for num2 in xrange(num + 1, LEN):
                            if count[num2]:
                                median = (num + num2) / float(2)
                                break
                    break
        max_cnt = max(count)
        for num, c in enumerate(count):
            if c == max_cnt:
                mode = num
                break
        # minimum, maximum, mean, median, and mode
        return map(float, [mn, mx, mean, median, mode])
