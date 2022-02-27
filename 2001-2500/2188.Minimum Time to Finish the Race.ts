function minimumFinishTime(tires: number[][], changeTime: number, numLaps: number): number {
    tires.sort((a, b) => a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]);
    let tireLapsTime = new Array(tires.length);
    function getBestReuseTime(laps: number) {
        let res = Infinity;
        for (let tireId = 0; tireId < tires.length; tireId++) {
            const [f, r] = tires[tireId];
            tireLapsTime[tireId] ||= [[f, f]];
            const lapsTime = tireLapsTime[tireId];
            while (lapsTime.length < laps && lapsTime[lapsTime.length - 1][1] < res && lapsTime[lapsTime.length - 1][0] < changeTime + f) {
                const nextLapTime = lapsTime[lapsTime.length - 1][0] * r;
                lapsTime.push([nextLapTime, lapsTime[lapsTime.length - 1][1] + nextLapTime]);
            }
            if (lapsTime.length >= laps) {
                res = Math.min(res, lapsTime[laps - 1][1]);
            }
        }
        return res + changeTime;
    }

    let dp = new Array(numLaps + 1);
    dp[0] = 0;
    let noNeedToInsist = false;
    for (let laps = 1; laps <= numLaps; laps++) {
        let res = Infinity;
        if (!noNeedToInsist) {
            res = getBestReuseTime(laps);
            if (res === Infinity) {
                noNeedToInsist = true;
            }
        }
        for (let thisLaps = 1; thisLaps <= laps / 2; thisLaps++) {
            const remainLaps = laps - thisLaps;
            res = Math.min(res, dp[remainLaps] + dp[thisLaps]);
        }
        dp[laps] = res;
    }

    return dp[numLaps] - changeTime;
};

