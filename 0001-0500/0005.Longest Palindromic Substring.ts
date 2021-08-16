function longestPalindrome(s: string): string {
    s = '#' + s.split('').join('#') + '#';
    const p:number[] = [];
    let maxRight = -1, center = -1;
    for (let i = 0; i < s.length; i++) {
        let l:number, r:number;
        if (i > maxRight) {
            l = i - 1;
            r = i + 1;
        } else {
            const j = center + center - i;
            l = i - Math.ceil(p[j] / 2);
            r = i + Math.ceil(p[j] / 2);
            if (r > maxRight) {
                l += r - maxRight - 1;
                r = maxRight + 1;
            }
        }
        while (0 <= l && r < s.length && s[l] === s[r]) {
            l--; r++;
        }
        p.push(r - l - 1);
        if (r - 1 > maxRight) {
            maxRight = r - 1;
            center = i;
        }
    }
    const maxP = Math.floor(Math.max(...p));
    const maxCenter = p.indexOf(maxP);
    return s.slice(maxCenter - Math.floor(maxP / 2), maxCenter + Math.ceil(maxP / 2)).split('#').join('');
};

