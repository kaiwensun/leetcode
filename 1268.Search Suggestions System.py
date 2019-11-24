import collections
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        def dfs(p, res):
            if '#' in p:
                for _ in xrange (p['#'][1]):
                    if len(res) == 3:
                        break
                    res.append(p['#'][0])
            if len(res) == 3:
                return res
            for key in sorted(p.keys()):
                if key != "#" and len(dfs(p[key], res)) == 3:
                    return res
            return res
        
        T = lambda: collections.defaultdict(T)
        trie = T()
        for product in products:
            p = trie
            for c in product:
                p = p[c]
            p["#"] = (product, p["#"][1] + 1 if "#" in p else 1)
        res = []
        p = trie
        for c in searchWord:
            p = p[c]
            res.append(dfs(p, []))
        return res
