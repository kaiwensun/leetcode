function minCapability(nums: number[], k: number): number {
    function test(nums: number[], mx: number, k: number) {
        let cnt = 0;
        for (let i = 0; i < nums.length; i++) {
            if (nums[i] <= mx) {
                cnt++;
                if (cnt === k) {
                    return true;
                }
                i++;
            }
        }
        return false;
    }

    let l = Math.min(...nums), r = Math.max(...nums) + 1;
    while (l < r) {
        const mid = Math.floor((l + r) / 2);
        if (test(nums, mid, k)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
};

