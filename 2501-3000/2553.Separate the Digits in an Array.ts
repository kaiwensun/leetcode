function separateDigits(nums: number[]): number[] {
    const res: number[] = [];
    nums.forEach(num => [...("" + num)].forEach(c => res.push(parseInt(c))));
    return res;
};

