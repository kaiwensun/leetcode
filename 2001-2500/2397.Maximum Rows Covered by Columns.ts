function maximumRows(matrix: number[][], numSelect: number): number {
    const M = matrix.length, N = matrix[0].length;
    const ones = new Array(M);
    for (let i = 0; i < M; i++) {
        ones[i] = matrix[i].reduce((acc, num) => acc + num, 0);
    }
    return (function dfs(j: number, cols: number): number {
        if (cols === 0) {
            return ones.filter(one => one === 0).length;
        }
        if (j === N) {
            return 0;
        }
        let res = dfs(j + 1, cols);
        let covered = 0;
        for (let i = 0; i < M; i++) {
            ones[i] -= matrix[i][j];
        }
        res = Math.max(res, covered + dfs(j + 1, cols - 1));
        for (let i = 0; i < M; i++) {
            ones[i] += matrix[i][j];
        }
        return res;
    })(0, numSelect);
};

