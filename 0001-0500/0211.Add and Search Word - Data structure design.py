from collections import defaultdict
class WordDictionary(object):
    

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: defaultdict(Trie)
        self.trie = Trie()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        p = self.trie
        for c in word:
            p = p[c]
        p["#"] = word
        

    def search(self, word, index=0, p=None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if p is None:
            p = self.trie
        if index == len(word):
            return "#" in p
        else:
            if word[index] == ".":
                for c in p.keys():
                    if c == "#":
                        continue
                    if self.search(word, index + 1, p[c]):
                        return True
                return False
            else:
                return word[index] in p and self.search(word, index + 1, p[word[index]])
                        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
