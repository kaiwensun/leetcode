function beautifulSubarrays(nums: number[]): number {
    let xor = 0;
    let res = 0;
    const cnt = {0: 1};
    for (const num of nums) {
        xor ^= num;
        cnt[xor] ||= 0;
        res += cnt[xor];
        cnt[xor] += 1;
    }
    return res;
};

