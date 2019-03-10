class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()
        x_p = y_p = 1
        while x_p + y_p <= bound:
            while x_p + y_p <= bound:
                result.add(x_p + y_p)
                y_p *= y
                if y == 1:
                    break
            x_p *= x
            y_p = 1
            if x == 1:
                break
        return list(result)
            
            
