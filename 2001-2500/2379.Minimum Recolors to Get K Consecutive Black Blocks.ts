function minimumRecolors(blocks: string, k: number): number {
    const cnt = {'W': 0, 'B': 0};
    let res = Infinity;
    [...blocks].forEach((c, i) => {
        cnt[c] += 1;
        if (i - k + 1 >= 0) {
            res = Math.min(res, cnt.W);
            cnt[blocks[i - k + 1]] -= 1;
        }
    });
    return res;
};

