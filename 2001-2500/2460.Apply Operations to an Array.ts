function applyOperations(nums: number[]): number[] {
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            nums[i++] *= 2;
            nums[i] = 0;
        }
    }
    let j = 0;
    for (let i = 0, j = 0; i < nums.length; i++) {
        if (nums[i] !== 0) {
            let tmp = nums[i]; nums[i] = 0; nums[j++] = tmp;
        }
    }
    return nums;
};

