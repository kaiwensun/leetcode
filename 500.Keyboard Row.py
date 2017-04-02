class Solution(object):
    def __init__(self):
        self.dic = dict(zip("qwertyuiop",[1]*10));
        self.dic.update(zip("asdfghjkl",[2]*9));
        self.dic.update(zip("zxcvbnm",[3]*7));
    
    def findWords(self, words):
        return filter(
            lambda word:
                len(word)==len(filter(lambda g:g==self.dic[word[0].lower()],map(lambda c:self.dic[c],word.lower())))
            ,words
        )
