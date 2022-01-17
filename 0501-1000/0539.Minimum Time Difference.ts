function findMinDifference(timePoints: string[]): number {
    const times = timePoints.map(timePoint => parseInt(timePoint.substring(0, 2)) * 60 + parseInt(timePoint.substring(3, 5)));
    times.sort((a, b) => a - b);
    times.push(times[0] + 24 * 60);
    let res = Infinity;
    for (let i = 0; i < times.length - 1; i++) {
        res = Math.min(res, times[i + 1] - times[i]);
    }
    return res;
};

