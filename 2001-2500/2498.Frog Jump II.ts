function maxJump(stones: number[]): number {
    let res = 0;
    for (let i = 1; i < stones.length; i++) {
        res = Math.max(res, stones[i] - stones[Math.max(0, i - 2)]);
    }
    return res;
};

