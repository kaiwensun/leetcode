function findFinalValue(nums: number[], original: number): number {
    const set = new Set(nums);
    while (set.has(original)) {
        original *= 2;
    }
    return original;
};

