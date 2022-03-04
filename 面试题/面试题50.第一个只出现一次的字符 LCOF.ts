function firstUniqChar(s: string): string {
    const cnt = {'': 0};
    [].forEach.call(s, (c: string) => {
        cnt[c] ||= 0;
        cnt[c]++;
    });
    for (let i = 0; i < s.length; i++) {
        if (cnt[s[i]] === 1) {
            return s[i];
        }
    }
    return " ";
};


