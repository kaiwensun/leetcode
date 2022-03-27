function hasAlternatingBits(n: number): boolean {
    let cur = 1 - (n & 1);
    while (n) {
        if (!(n & 1 ^ cur)) return false;
        cur = n & 1;
        n >>= 1;
    }
    return true;
};

