function rowAndMaximumOnes(mat: number[][]): number[] {
    const arr = mat.map(row => row.reduce((acc, num) => acc + num, 0));
    const mx = Math.max(...arr);
    return [arr.indexOf(mx), mx];
};

