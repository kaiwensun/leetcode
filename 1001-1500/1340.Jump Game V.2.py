# https://leetcode.com/problems/jump-game-v/discuss/496891/Almost-O(N)-solution-with-detailed-explanation

from collections import deque

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        def add_target_to_wards(wards, index, target):
            if not wards[index] or arr[wards[index][0]] == arr[target]:
                wards[index].append(target)
            else:
                wards[index] = [target]

        def flush(wards, queue, direction):
            for i in range(len(queue) - 1):
                add_target_to_wards(wards, queue[i], queue[i + 1])
        
        def calcResult(index):
            if res[index] is None:
                res[index] = 1
                for is_left_wards in range(2):
                    for target in wards[is_left_wards][index]:
                        res[index] = max(res[index], 1 + calcResult(target))
            return res[index]
        
        def calcWards():
            for is_left_wards in range(2):
                window = deque()
                order = reversed if is_left_wards else lambda x:x
                for i, a in order(tuple(enumerate(arr))):
                    if window and ((not is_left_wards and window[0] < i - d) or (is_left_wards and window[0] > i + d)):
                        x = window.popleft()
                        if window:
                            add_target_to_wards(wards[is_left_wards], x, window[0])
                    while window and arr[window[-1]] <= a:
                        x = window.pop()
                        if window:
                            add_target_to_wards(wards[is_left_wards], window[-1], x)
                    window.append(i)
                flush(wards[is_left_wards], window, 1)
        
        wards = [[list() for _ in arr] for __ in range(2)]
        res = [None] * len(arr)
        
        calcWards()
        return max(calcResult(index) for index in range(len(arr)))
