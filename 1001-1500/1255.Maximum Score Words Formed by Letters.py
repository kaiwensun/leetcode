import functools, collections
class Solution:
    def maxScoreWords(self, words, letters, score) -> int:
        @functools.lru_cache(None)
        def dp(word_index, counter):
            if word_index < 0:
                return 0
            word = words[word_index]
            new_counter = deduct_word_from_counter(word, counter)
            res = 0
            if new_counter:
                res = calc_score(word) + dp(word_index - 1, new_counter)
            res = max(res, dp(word_index - 1, counter))
            return res 
        def calc_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        def deduct_word_from_counter(word, counter):
            cnt = collections.Counter(word)
            for l, c in cnt.items():
                if counter[ord(l) - ord('a')] < c:
                    return None
            return tuple(counter[i] - cnt[chr(i + ord('a'))] for i in range(len(counter)))
        def letters2counter(letters):
            cnt = collections.Counter(letters)
            return tuple(cnt[chr(i + ord('a'))] for i in range(26))
        return dp(len(words) - 1, letters2counter(letters))
