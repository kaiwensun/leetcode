function findKDistantIndices(nums: number[], key: number, k: number): number[] {
    let prevEnd = -1, res = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === key) {
            let start = Math.max(0, i - k);
            let end = Math.min(nums.length - 1, i + k);
            if (prevEnd >= start) {
                start = prevEnd + 1;
            }
            for (let j = start; j <= end; j++) {
                res.push(j);
            }
            prevEnd = end;
        }
    }
    return res;
};

