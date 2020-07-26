class Solution(object):
    codes = {
            int('10000000', 2): (int('00000000', 2), 1),
            int('11100000', 2): (int('11000000', 2), 2),
            int('11110000', 2): (int('11100000', 2), 3),
            int('11111000', 2): (int('11110000', 2), 4)
        }
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            length = self.get_length(data[i])
            if length == -1:
                return False
            for j in xrange(length - 1):
                i += 1
                if i == len(data):
                    return False
                if not self.check_10(data[i]):
                    return False
            i += 1
        return True
            
    def get_length(self, data):
        for key, value in self.codes.iteritems():
            if key & data == value[0]:
                return value[1]
        return -1

    def check_10(self, data):
        return int('11000000', 2) & data == int('10000000', 2)
