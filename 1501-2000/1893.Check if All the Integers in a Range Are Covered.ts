function isCovered(ranges: number[][], left: number, right: number): boolean {
    ranges.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    let cur = left;
    for (let [start, end] of ranges) {
        if (start > cur) return false;
        cur = Math.max(cur, end + 1);
        if (cur > right) return true;
    }
    return false;
};

