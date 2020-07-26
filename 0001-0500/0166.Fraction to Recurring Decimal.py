class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = numerator / denominator >= 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        integral = numerator / denominator
        remaind = numerator % denominator
        if remaind == 0:
            return ('' if sign else '-') + str(integral)
        bit = 0
        decimal = ''
        remaind2bit = {}
        while remaind != 0 and remaind not in remaind2bit:
            remaind2bit[remaind] = bit
            remaind *= 10
            decimal = decimal + str(remaind / denominator)
            remaind = remaind % denominator
            bit += 1
        if remaind != 0:
            decimal = decimal[:remaind2bit[remaind]] + '(' + decimal[remaind2bit[remaind]:] + ')'
        return ('' if sign else '-') + str(integral) + '.' + decimal
