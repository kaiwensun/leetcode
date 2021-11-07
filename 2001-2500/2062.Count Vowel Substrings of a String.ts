function countVowelSubstrings(word: string): number {
    const vowels = 'aeiou'.split('');
    const cnt = {};
    vowels.map(c => cnt[c] = 0);
    let res = 0, preStart = 0, l = 0;
    for (let r = 0; r <= word.length; r++) {
        if (r < word.length && 'aeiou'.includes(word[r])) {
            cnt[word[r]]++;
            while (cnt[word[l]] > 1) {
                cnt[word[l++]]--;
            }
            if (Object.values(cnt).filter(v => v).length == vowels.length) {
                res += l - preStart + 1;
            }
        } else {
            vowels.map(c => cnt[c] = 0);
            preStart = l = r + 1;
        }
    }
    return res;
};

