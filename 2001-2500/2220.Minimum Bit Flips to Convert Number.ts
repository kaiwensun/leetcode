function minBitFlips(start: number, goal: number): number {
    let xor = start ^ goal;
    let res = 0;
    while (xor) {
        res++;
        xor &= (xor - 1);
    }
    return res;
};

