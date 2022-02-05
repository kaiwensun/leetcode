function minimumSum(num: number): number {
    const digits = ('' + num).split('').sort().map(d => parseInt(d));
    let res = 0, i = 0;
    while (i < digits.length) {
        res *= 10;
        res += digits[i++];
        res += digits[i++];
    }
    return res;
};

