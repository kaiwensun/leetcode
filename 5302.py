from collections import defaultdict

T = lambda: defaultdict(T)

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.enc_dict = dict(zip(keys, values))
        self.dec_dict = defaultdict(list)
        for i in range(len(values)):
            self.dec_dict[values[i]].append(keys[i])
        self.trie = T()
        for word in dictionary:
            p = self.trie
            for c in word:
                p = p[c]
            p["#"] = True


    def encrypt(self, word1: str) -> str:
        return "".join([self.enc_dict[c] for c in word1])


    def decrypt(self, word2: str) -> int:
        def dfs(p, i):
            if i == len(word2):
                return 1 if p["#"] else 0
            cc = word2[i: i + 2]
            candidates = self.dec_dict[cc]
            return sum(dfs(p[candidate], i + 2) for candidate in candidates if candidate in p)
        return dfs(self.trie, 0)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

