function countDistinct(nums: number[], k: number, p: number): number {
    let cnt = 0, left = 0;
    const res = new Set();
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % p === 0) {
            cnt++;
        }
        while (cnt > k) {
            if (nums[left++] % p === 0) {
                cnt--;
            }
        }
        for (let start = left; start <= i; start++) {
            res.add('' + nums.slice(start, i + 1));
        }
    }
    return res.size;
};

