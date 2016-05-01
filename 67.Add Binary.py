class Solution(object):
    res_table = [[[0,1],[1,0]],[[1,0],[0,1]]]
    car_table = [[[0,0],[0,1]],[[0,1],[1,1]]]
    def addBinary(self, a, b):
        l = max(len(a),len(b))+1
        a=map(lambda x:int(x),'0'*(l-len(a))+a)
        b=map(lambda x:int(x),'0'*(l-len(b))+b)
        rtn = [0]*l
        c = 0 #c for carry
        for i in xrange(-1,-l-1,-1):
            rtn[i]=self.res_table[a[i]][b[i]][c]
            c=self.car_table[a[i]][b[i]][c]
        try:
            return "".join(map(lambda x:str(x),rtn[rtn.index(1):]))
        except ValueError:
            return '0'

