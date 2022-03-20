function maximumBobPoints(numArrows: number, aliceArrows: number[]): number[] {
    let maxScore = -Infinity;
    let maxSolution = undefined;
    (function dfs(bobNumArrows: number, section: number, curScore: number, curSolution: number[]) {
        if (bobNumArrows < 0) {
            throw bobNumArrows;
        }
        if (section === aliceArrows.length) {
            if (curScore > maxScore) {
                maxScore = curScore;
                maxSolution = curSolution.slice();
                maxSolution[0] += bobNumArrows;
            }
            return 0;
        }
        curSolution.push(0);
        dfs(bobNumArrows, section + 1, curScore, curSolution);
        curSolution.pop();
        if (aliceArrows[section] < bobNumArrows) {
            const cost = aliceArrows[section] + 1;
            curSolution.push(cost);
            dfs(bobNumArrows - cost, section + 1, curScore + section, curSolution);
            curSolution.pop();
        }
    })(numArrows, 0, 0, []);
    return maxSolution;
};

