import itertools

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        list_of_lists = map(lambda word: filter(len, word.split(separator)), words)
        return list(itertools.chain.from_iterable(list_of_lists))

