function minimumDeletions(nums: number[]): number {
    const N = nums.length;
    if (N <= 1) {
        return N;
    }
    const min = Math.min(...nums);
    const max = Math.max(...nums);
    let id1 = nums.indexOf(min);
    let id2 = nums.indexOf(max);
    if (id1 > id2) {
        const tmp = id1; id1 = id2; id2 = tmp;
    }
    
    return Math.min(id2 + 1, id1 + 1 + N - id2, N - id1);
};

