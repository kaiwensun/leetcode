function countAsterisks(s: string): number {
    let res = 0, count = true;
    for (const c of s) {
        if (c === '|') {
            count = !count;
        } else if (c === '*' && count) {
            res++;
        }
    }
    return res;
};

