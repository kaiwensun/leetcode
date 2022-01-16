function minMoves(target: number, maxDoubles: number): number {
    let res = 0;
    while (target && maxDoubles) {
        maxDoubles--;
        res += (target & 1) + 1;
        target >>= 1;
    }
    return res + (target === 0 ? -1 : target) - 1;
};

