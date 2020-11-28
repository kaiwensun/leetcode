class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lengths = self._convert_di_to_lengths(S)
        right = len(S) + 1
        left = -1
        lengths[0] += 1
        direction = S[0]
        result = []
        for length in lengths:
            if direction == "I":
                result.extend(range(right - length, right))
                right -= length
                direction = "D"
            else:
                result.extend(range(left + length, left, -1))
                left += length
                direction = "I"
        return result
         
    def _convert_di_to_lengths(self, S):
        result = []
        counter = 0
        direction = S[0]
        for s in S:
            if s == direction:
                counter += 1
            else:
                result.append(counter)
                counter = 1
                direction = s
        result.append(counter)
        return result

