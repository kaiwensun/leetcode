class Solution(object):
    def maxCandies(self, opened, candies, keys, containedBoxes, initialBoxes):
        """
        :type opened: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        N = len(opened)
        boxes_to_open = initialBoxes
        res = 0
        opened_something = True
        while opened_something and boxes_to_open:
            index = 0
            opened_something = False
            while index < len(boxes_to_open):
                box_id = boxes_to_open[index]
                if opened[box_id]:
                    res += candies[box_id]
                    for key in keys[box_id]:
                        opened[key] = 1
                    boxes_to_open.extend(containedBoxes[box_id])
                    if index == len(boxes_to_open) - 1:
                        boxes_to_open.pop()
                    else:
                        boxes_to_open[index] = boxes_to_open.pop()
                    opened_something = True
                else:
                    index += 1
        return res
