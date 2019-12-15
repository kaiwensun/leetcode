class CombinationIterator(object):

    def __init__(self, characters, length):
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
        res = self.buffer
        try:
            self.buffer = next(self.generator)
        except StopIteration:
            self.buffer = None
        return res
        
    def hasNext(self):
        return self.buffer is not None
