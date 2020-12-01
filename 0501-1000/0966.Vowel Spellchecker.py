class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        def fix_vowel(word):
            return reduce(lambda w, v: w.replace(v, "_"), "aeiou", word.lower())

        dic_exact, dic_case, dic_vowel = set(wordlist), {}, {}
        for word in wordlist:
            dic_case.setdefault(word.lower(), word)
            dic_vowel.setdefault(fix_vowel(word), word)
        res = []
        for query in queries:
            if query in dic_exact:
                res.append(query)
            else:
                res.append(dic_case.get(query.lower(), dic_vowel.get(fix_vowel(query),"")))
        return res

