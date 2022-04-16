function findClosestNumber(nums: number[]): number {
    return nums.reduce(([diff, res], num) => {
        const abs = Math.abs(num);
        return abs < diff || (abs === diff && res < num) ? [abs, num] : [diff, res]
    }, [Infinity, undefined])[1];
};

