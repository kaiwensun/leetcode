import collections
class Solution(object):
    def displayTable(self, orders):
        foodNames = {}
        title = ["Table"]
        for order in orders:
            foodNames[(order[2])] = None
        for key in sorted(foodNames.keys()):
            foodNames[key] = len(title) - 1
            title.append(key)
        res = collections.defaultdict(lambda: [0] * len(foodNames))
        for order in orders:
            res[order[1]][foodNames[order[2]]] += 1
        table = [title]
        for key in sorted(res.keys(), key=int):
            value = map(str, res[key])
            row = [key]
            row.extend(value)
            table.append(row)
        return table
