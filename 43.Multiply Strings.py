"""
Though we can do

	return str(int(num1)*int(num2))

but let's to something more interesting!
"""
class Solution(object):
    multbl={}
    addtbl={}
    dic={}
    def init(self):
        self.multbl={}
        self.addtbl={}
        for a in xrange(10):
            for b in xrange(10):
                self.multbl[str(a)+str(b)]="%02d"%(a*b)
                self.addtbl[str(a)+str(b)]="%02d"%(a+b)
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        self.dic={}
        if self.multbl=={}:
            self.init()
        if len(num1)<len(num2):
            tmp=num1;num1=num2;num2=tmp;
        lst1 = list(num1)
        rtn = ['0']
        for i in xrange(len(num2)):
            prod = self.numTimesDigit(lst1,num2[-1-i])
            rtn = self.numAddNum(self.remove0(rtn),self.remove0(prod+['0']*i))
        return "".join(self.remove0(rtn))
    
    def remove0(self,lst):
        i=0
        while i<len(lst)-1:
            if lst[i]=='0':
                del lst[i]
            else:
                break
        return lst
        
    def numAddNum(self,num1,num2):
        rtn=[]
        if len(num1)>len(num2):
            tmp=num1;num1=num2;num2=tmp;
        carry = '0'
        for x in xrange(len(num1)):
            summation = self.addtbl[num1[-1-x]+num2[-1-x]]
            left = summation[0]
            right = summation[1]
            left = (self.addtbl[left+((self.addtbl[right+carry])[0])])[1]
            right = (self.addtbl[right+carry])[1]
            carry=left
            rtn.insert(0,right)

        if carry!='0':
            prefix = self.numAddNum('1',['0']+num2[0:len(num2)-len(num1)])
            rtn = prefix+rtn
        else:
            rtn = num2[0:len(num2)-len(num1)]+rtn
        return rtn
        
        
    def numTimesDigit(self,num,dig):
        """
        :type num: list[str]
        :type dig: str and len(dig)==1
        :rtype: list[str]
        """
        if dig in self.dic:
            return self.dic[dig]
        rtn = []
        carry='0'
        for x in xrange(len(num)-1,-1,-1):
            pro = self.multbl[num[x]+dig]
            summation=self.addtbl[pro[1]+carry]
            right = summation[1]
            carry = (self.addtbl[pro[0]+summation[0]])[1]
            rtn.insert(0,right)
        if carry!='0':
            rtn.insert(0,carry)
        self.dic[dig]=self.remove0(rtn)
        return rtn
