class CombinationIterator(object):

    def __init__(self, characters, length):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.generator = self.gen(characters, length)
        self.buffer = next(self.generator)
        

    def gen(self, characters, length):
        if length == 0:
            yield ""
        elif len(characters) == length:
            yield characters
        elif len(characters) > length:
            for tail in self.gen(characters[1:], length - 1):
                yield characters[0] + tail
            for tail in self.gen(characters[1:], length):
                yield tail
        
    def next(self):
        res, self.buffer = self.buffer, next(self.generator, None)
        return res
        

    def hasNext(self):
        return self.buffer is not None
        
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
