function countSubarrays(nums: number[], minK: number, maxK: number): number {
    if (minK > maxK) return 0;
    let res = 0;
    nums.push(Infinity);
    let start = 0;
    nums.forEach((num, end) => {
        if (num > maxK || num < minK) {
            if (start < end) {
                if (minK === maxK) {
                    res +=  (1 + end - start) * (end - start) / 2;
                } else {
                    let minInd = start - 1, maxInd = start - 1;
                    for (let i = start; i < end; i++) {
                        if (nums[i] === minK) minInd = i;
                        if (nums[i] === maxK) maxInd = i;
                        res += Math.min(maxInd, minInd) - start + 1;
                    }
                }
            }
            start = end + 1;
        }
    });
    return res;
};

