function countSubarrays(nums: number[], k: number): number {
    const med = nums.indexOf(k);
    if (med === -1) {
        return 0;
    }
    const rCnt:{ [key: string]: number; }  = {0: 1}, lCnt:{ [key: string]: number; } = {0: 1};
    let diff = 0;
    for (let i = med + 1; i < nums.length; i++) {
        diff += Math.sign(nums[i] - k);
        rCnt[diff] ||= 0;
        rCnt[diff]++;
    }
    diff = 0;
    for (let i = med - 1; i >= 0; i--) {
        diff += Math.sign(nums[i] - k);
        lCnt[diff] ||= 0;
        lCnt[diff]++;
    }
    let res = 0;
    for (const [key, l] of Object.entries(lCnt)) {
        res += l * (rCnt[-parseInt(key)] || 0);
        res += l * (rCnt[1 - parseInt(key)] || 0);
    }
    return res;
};

