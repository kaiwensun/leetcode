from collections import Counter
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        self.p = 0
        self.formula = formula
        def readOneThing():
            result = ''
            typ = None
            while self.p < len(self.formula):
                c = self.formula[self.p]
                if c == '(' or c == ')':
                    if typ is None:
                        result = c
                        self.p += 1
                    break
                elif '0' <= c and c <= '9':
                    if typ is None or typ == int:
                        typ = int
                        result += c
                        self.p += 1
                    else:
                        break
                elif 'A' <= c and c <= 'Z':
                    if typ is None:
                        typ = str
                        result += c
                        self.p += 1
                    else:
                        break
                else:
                    result += c  
                    self.p += 1
            return result
                        
        
        def nextIsNum():
            return '0' <= self.formula[self.p] and self.formula[self.p] <= '9'

        def readASequence():
            """
            A sequence is in one of the following form:
            (.....)13
            Element13
            """
            counter = Counter()
            c = readOneThing()
            if c == '(':
                counter = Counter()
                while self.formula[self.p] != ')':
                    counter += readASequence()
                readOneThing()
                if self.p < len(self.formula) and nextIsNum():
                    multi = int(readOneThing())
                    for k in counter:
                        counter[k] = counter[k] * multi
            else:
                if self.p < len(self.formula) and nextIsNum():
                    multi = int(readOneThing())
                else:
                    multi = 1
                counter[c] = multi
            return counter
        
        def sortOutput(counter):
            lst = sorted(list(counter.iteritems()))
            return ''.join([oneElemCnt(k, v) for k, v in lst])
            
        def oneElemCnt(k, v):
            if v == 1:
                return k
            return "%s%s" % (k, v)

        counter = Counter()
        while self.p < len(self.formula):
            tmp = readASequence()
            print tmp
            counter += tmp
        
        return sortOutput(counter)
                        
                        
