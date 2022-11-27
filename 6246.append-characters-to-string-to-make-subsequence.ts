function appendCharacters(s: string, t: string): number {
    let j = 0;
    for (let i = 0; i < t.length; i++) {
        while (j < s.length && s[j] !== t[i]) {
            j++;
        }
        if (j === s.length) {
            return t.length - i;
        } else {
            j++;
        }
    }
    return 0;
};

