function minMaxGame(nums: number[]): number {
    let len = nums.length / 2;
    while (len >= 1) {
        for (let i = 0; i < len; i++) {
            const func = i % 2 ? Math.max : Math.min;
            nums[i] = func(nums[i * 2], nums[i * 2 + 1]);
        }
        len /= 2;
    }
    return nums[0];
};

