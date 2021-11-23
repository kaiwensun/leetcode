function originalDigits(s: string): string {
    const features: [number, string, string][] = [
        [0, "z", "zero"],
        [6, "x", "six"],
        [2, "w", "two"],
        [7, "s", "seven"],
        [5, "v", "five"],
        [4, "f", "four"],
        [3, "r", "three"],
        [8, "h", "eight"],
        [9, "i", "nine"],
        [1, "o", "one"]
    ];
    const counter = {};
    for (let i = 0; i < 26; i++) {
        counter[String.fromCharCode(97 + i)] = 0;
    }
    for (let i = 0; i < s.length; i++) {
        counter[s[i]]++;
    }
    let n = s.length;
    let res:number[] = [];
    while (n) {
        for (let [num, key, eng] of features) {
            const cnt = counter[key];
            for (let c of eng) {
                counter[c] -= cnt;
            }
            n -= cnt * eng.length;
            for (let i = 0; i < cnt; i++) {
                res.push(num);
            }
        }
    }
    return res.sort().join('');
};

