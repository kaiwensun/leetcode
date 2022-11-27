function countPalindromes(s: string): number {
    const MOD = 10 ** 9 + 7;
    const digits = new Set(s);

    function assignDP2(i: number, dp1, dp2) {
        for (const digit of Object.keys(counter)) {
            const string = s[i] + digit;
            counter2[string] ||= 0;
            counter2[string] += counter[digit] || 0;
            counter2[string] %= MOD;
            dp2[i] = {...counter2};
        }
        counter[s[i]] ||= 0;
        counter[s[i]]++;
        dp1[i] = {...counter};
    }

    const leftDP = new Array(s.length), leftDP2 = new Array(s.length);
    let counter = {}, counter2 = {};
    for (let i = 0; i < s.length; i++) {
        assignDP2(i, leftDP, leftDP2);
    }

    const rightDP = new Array(s.length), rightDP2 = new Array(s.length);
    counter = {}, counter2 = {};
    for (let i = s.length - 1; i >= 0; i--) {
        assignDP2(i, rightDP, rightDP2);
    }
    let res = 0;
    for (let i = 2; i < s.length - 2; i++) {
        for (const d1 of digits) for (const d2 of digits) {
            const string = d1 + d2;
            res += (leftDP2[i - 1][string] || 0) * (rightDP2[i + 1][string] || 0);
            res %= MOD;
        }
    }
    return res;
};

