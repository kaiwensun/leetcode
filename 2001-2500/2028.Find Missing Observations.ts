function missingRolls(rolls: number[], mean: number, n: number): number[] {
    const m = rolls.length;
    let sum = mean * (m + n);
    for (let roll of rolls) {
        sum -= roll;
    }
    const res = [];
    if (sum < n || sum > n * 6 ) {
        return [];
    }
    for (let i = 0; i < n; i++) {
        const roll = Math.floor(sum / (n - i));
        res.push(roll);
        sum -= roll;
    }
    return res;
};

