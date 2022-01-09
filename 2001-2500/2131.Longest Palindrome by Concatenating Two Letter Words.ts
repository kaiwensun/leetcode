function longestPalindrome(words: string[]): number {
    const cnt = {};
    for (const word of words) {
        cnt[word] ||= 0;
        cnt[word] += 1;
    }
    let res = 0;
    let singlePalindrome = false;
    for (const word of words) {
        const reverse = word[1] + word[0];
        let c: number;
        if (reverse === word) {
            singlePalindrome ||= cnt[word] % 2 === 1;
            c = Math.floor(cnt[word] / 2);
        } else if (cnt[reverse] !== undefined) {
            c = Math.min(cnt[word], cnt[reverse]);
        } else {
            continue;
        }
        res += c * 4;
        cnt[word] -= c;
        cnt[reverse] -= c;
    }
    res += singlePalindrome ? 2 : 0;
    return res;
};

