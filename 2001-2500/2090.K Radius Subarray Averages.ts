function getAverages(nums: number[], k: number): number[] {
    const res = Array(nums.length);
    let l = 0, r = 0, sum = 0;
    for (let i = 0; i < nums.length; i++) {
        while (r <= i + k && r < nums.length) {
            sum += nums[r++];
        }
        if (l < i - k) {
            sum -= nums[l++];
        }
        res[i] = r - l < k + k + 1 ? -1 : Math.floor(sum / (r - l));
    }
    return res;
};

