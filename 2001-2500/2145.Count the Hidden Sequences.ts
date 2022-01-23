function numberOfArrays(differences: number[], lower: number, upper: number): number {
    let val = 0, min = 0, max = 0;
    for (let diff of differences) {
        val += diff;
        min = Math.min(min, val);
        max = Math.max(max, val);
    }
    return Math.max(0, (upper - lower) - (max - min) + 1);
};

