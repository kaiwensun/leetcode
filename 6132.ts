function minimumOperations(nums: number[]): number {
    return (new Set(nums.filter(_ => _))).size;
};

