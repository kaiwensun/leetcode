function firstCompleteIndex(arr: number[], mat: number[][]): number {
    const M = mat.length;
    const N = mat[0].length;
    const rows = new Array(M);
    for (let i = 0; i < M; i++) { rows[i] = new Set(); }
    const cols = new Array(N);
    for (let j = 0; j < N; j++) { cols[j] = new Set(); }
    const num2cord = {};
    for (let i = 0; i < M; i++) {
        for (let j = 0; j < N; j++) {
            const num = mat[i][j];
            rows[i].add(num);
            cols[j].add(num);
            num2cord[num] = [i, j]
        }
    }
    for (let k = 0; k < arr.length; k++) {
        const num = arr[k];
        const [i, j] = num2cord[num];
        rows[i].delete(num);
        cols[j].delete(num);
        if (!rows[i].size || !cols[j].size) {
            return k;
        }
    }
    return -1;
};

