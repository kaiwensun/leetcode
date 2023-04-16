declare global {
  interface Array<T> {
    snail(rowsCount: number, colsCount: number): number[][];
  }
}

Array.prototype.snail = function(rowsCount: number, colsCount: number): number[][] {
    const total = rowsCount * colsCount;
    if (this.length != total) return [];
    const res = new Array(rowsCount);
    for (let i = 0; i < rowsCount; i++) {
        res[i] = new Array(colsCount);
    }
    function nextIndex(i: number, j: number) {
        if ((j % 2 && i === 0) || (j % 2 === 0 && i === rowsCount - 1)) {
            return [i, j + 1];
        }
        return j % 2 ? [i - 1, j] : [i + 1, j];
    }
    let i = 0, j = 0;

    for (let k = 0; k < total; k++) {
        res[i][j] = this[k];
        [i, j] = nextIndex(i, j);
    }
    return res;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */

