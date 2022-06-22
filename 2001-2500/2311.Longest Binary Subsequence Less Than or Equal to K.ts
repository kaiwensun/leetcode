function longestSubsequence(s: string, k: number): number {
    let num = 0, res = 0, bit = 1;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === '0') {
            res ++;
            if (bit <= k) {
                bit <<= 1;
            }
        } else if (bit + num <= k) {
            res++;
            num += bit;
            bit <<= 1;
        }
    }
    return res;
};

