function pivotArray(nums: number[], pivot: number): number[] {
    const bigger = [];
    let j = 0;
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (num < pivot) {
            nums[j++] = num;
        } else if (num > pivot) {
            bigger.push(num);
        }
    }
    while (j < nums.length - bigger.length) {
        nums[j++] = pivot;
    }
    for (let i = 0; i < bigger.length; i++) {
        nums[j++] = bigger[i];
    }
    return nums;
};

