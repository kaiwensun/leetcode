import collections, math

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        ROW_SIZE = max([int(math.sqrt(len(num))), 20])
        arr = list(map(int, num))
        table = [arr[i: i + ROW_SIZE] for i in range(0, len(arr), ROW_SIZE)]
        row_size = [ROW_SIZE] * len(table)
        tracker = collections.defaultdict(collections.deque)
        for index, a in enumerate(arr):
            tracker[a].append(index)
        
        def getPseudoIndex(actual_index):
            pseudo_index = 0
            row_index = actual_index // ROW_SIZE
            index_in_row = actual_index % ROW_SIZE
            for i in range(0, row_index):
                pseudo_index += row_size[i]
            _, cnt = getPseudoIndexInRow(table[row_index], 0, index_in_row)
            pseudo_index += cnt
            return pseudo_index
        
        def deleteAtActualIndex(actual_index):
            row_index = actual_index // ROW_SIZE
            index_in_row = actual_index % ROW_SIZE
            table[row_index][index_in_row] = - index_in_row - 1
            row_size[row_index] -= 1

        def getPseudoIndexInRow(row, i, actual_index):
            """
            return [next index that has content, count]
            """
            if i == actual_index:
                return i, 0
            if row[i] < 0:
                j, pseudo_index = getPseudoIndexInRow(row, -row[i], actual_index)
                row[i] = -j
                return j, pseudo_index
            else:
                j, pseudo_index = getPseudoIndexInRow(row, i + 1, actual_index)
                return i, pseudo_index + 1
            
            
        def getMin(smaller_than, last_ok_pseudo_index):
            """
            return number, actual_index, pseudo_index
            """
            for d in range(smaller_than):
                if tracker[d] and (pseudo_index := getPseudoIndex(tracker[d][0])) <= last_ok_pseudo_index:
                    return d, tracker[d][0], pseudo_index
            return smaller_than, tracker[smaller_than][0], 0

        def collectRemainingTable():
            return sum(map(list, map(lambda row: filter(lambda x: x >= 0, row), table)), [])
        
        def getFirst(start_actual_index):
            start_row_index = start_actual_index // ROW_SIZE
            start_index_in_row = start_actual_index % ROW_SIZE
            row_index, index_in_row = start_row_index, start_index_in_row
            index_in_row = getNextInRow(table[row_index], start_index_in_row)
            while index_in_row == len(table[row_index]):
                row_index += 1
                start_index_in_row = 0
                if row_index == len(table):
                    break
                index_in_row = getNextInRow(table[row_index], start_index_in_row)
            if row_index == len(table):
                return -1, -1
            return table[row_index][index_in_row], row_index * ROW_SIZE + index_in_row
                
        def getNextInRow(row, i):
            if i >= len(row):
                return len(row)
            if row[i] >= 0:
                return i
            else:
                row[i] = -getNextInRow(row, i + 1)
                return -row[i]
            
        res = []
        arr = list(map(int, num))
        smaller_than, start_actual_index = table[0][0], 0
        while k > 0 and start_actual_index != -1:
            mn, mn_actual_index, mn_pseudo_index = getMin(smaller_than, k)
            tracker[mn].popleft()
            res.append(mn)
            deleteAtActualIndex(mn_actual_index)
            k -= mn_pseudo_index
            smaller_than, start_actual_index = getFirst(start_actual_index)
        res.extend(collectRemainingTable())
        return "".join(map(str, res))
