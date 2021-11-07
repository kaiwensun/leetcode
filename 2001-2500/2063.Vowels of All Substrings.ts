function countVowels(word: string): number {
    let res = 0;
    for (let i = 0; i < word.length; i++) {
        if ('aeiou'.includes(word[i])) {
            res += (i + 1) * (word.length - i);
        }
    }
    return res;
};

