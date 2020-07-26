class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        data = sorted([[a, 'a'], [b, 'b'], [c, 'c']])
        data[2][0] = min((data[0][0] + data[1][0]) * 2 + 2, data[2][0]) 
        res = [data[2][1]] * data[2][0]
        i = 2
        while i < len(res) and (data[1][0] or data[0][0]):
            if data[0][0] > data[1][0]:
                res.insert(i, data[0][1])
                data[0][0] -= 1
            else:
                res.insert(i, data[1][1])
                data[1][0] -= 1
            i += 3
        extra = data[1][0] - data[0][0]
        i = 0
        while i < len(res) and data[1][0] > data[0][0]:
            if i == 0 or i == 1:
                data[1][0] -= 1
                res.insert(i, data[1][1])
            elif (res[i - 1] == data[1][1]):
                if res[i] != data[1][1] and res[i - 2] != data[1][1]:
                    data[1][0] -= 1
                    res.insert(i, data[1][1])
            else:
                data[1][0] -= 1
                res.insert(i, data[1][1])
            i += 1
        res.append((data[0][1] + data[1][1]) * min(data[0][0], data[1][0]))
        if data[0][0] > data[1][0]:
            res.append(data[0][1])
        if data[0][0] < data[1][0]:
            res.append(data[1][1])
        return "".join(res)
