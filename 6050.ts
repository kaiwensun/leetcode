function appealSum(s: string): number {
    function calcLetter(target) {
        let res = 0, last = -1;
        [...s].forEach((c, i) => {
            if (c === target) {
                res += (i - last) * (i - last - 1) / 2;
                last = i;
            }
        });
        res += (n - last) * (n - last - 1) / 2;
        return complete - res;
    }
    const n = s.length;
    const complete = (1 + n) * n / 2;
    return [..."qwertyuiopasdfghjklzxcvbnm"].reduce((acc, c) => acc + calcLetter(c), 0);
};

