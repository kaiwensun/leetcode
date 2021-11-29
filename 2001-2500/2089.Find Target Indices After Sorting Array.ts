function targetIndices(nums: number[], target: number): number[] {
    let smaller = 0, equal = 0;
    nums.forEach(num => {
        if (num === target) equal++;
        else if (num < target) smaller++;
    });
    const res = Array(equal);
    for (let i = 0; i < equal; i++) {
        res[i] = i + smaller;
    }
    return res;
};

