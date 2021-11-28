function minCost(startPos: number[], homePos: number[], rowCosts: number[], colCosts: number[]): number {
    const delta = [Math.sign(homePos[0] - startPos[0]), Math.sign(homePos[1] - startPos[1])];
    const costs = [rowCosts, colCosts];
    let res = 0;
    for (let i = 0; i < 2; i++) {
        for (let j = startPos[i]; j !== homePos[i];) {
            j += delta[i]
            res += costs[i][j]
        }
    }
    return res;
};

