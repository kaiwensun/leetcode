/**
 * @param {number[][]} A
 * @return {number}
 */
var minFallingPathSum = function(A) {
    let M = A.length;
    let N = A[0].length;
    let row = A[0];
    for (let i = 1; i < M; i++) {
        let next_row = new Array(A[0].length);
        for (let j = 0; j < N; j++) {
            next_row[j] = 1 / 0;
            for (let jj = Math.max(0, j - 1); jj <= Math.min(N - 1, j + 1); jj++) {
                next_row[j] = Math.min(next_row[j], row[jj]);
            }
            next_row[j] += A[i][j];
        }
        row = next_row;
    }
    return Math.min(...row);
};

