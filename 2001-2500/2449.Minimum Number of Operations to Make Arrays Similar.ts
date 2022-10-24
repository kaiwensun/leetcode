function makeSimilar(nums: number[], target: number[]): number {
    function makeOneSimilar(nums: number[], target: number[]) {
        nums.sort((a, b) => a - b);
        target.sort((a, b) => a - b);
        let res = 0;
        for (let i = 0; i < nums.length; i++) {
            res += Math.abs(target[i] - nums[i]);
        }
        return res / 4;
    }
    return makeOneSimilar(nums.filter(n => n % 2), target.filter(n => n % 2)) +
        makeOneSimilar(nums.filter(n => n % 2 === 0), target.filter(n => n % 2 === 0));
};

