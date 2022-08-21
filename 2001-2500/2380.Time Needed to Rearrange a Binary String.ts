function secondsToRemoveOccurrences(s: string): number {
    let res = 0, cnt0 = 0;
    for (const c of s) {
        if (c === '0') {
            cnt0++;
        } else if (cnt0) {
            res = Math.max(res + 1, cnt0);
        }
    }
    return res;
};

