function minimumTime(time: number[], totalTrips: number): number {
    function test(totalTime) {
        let res = 0;
        for (let t of time) {
            res += Math.floor(totalTime / t);
        }
        return res >= totalTrips;
    }
    let l = 0, r = totalTrips * Math.min(...time) + 1;
    while (l < r) {
        const mid = Math.floor((l + r) / 2);
        if (test(mid)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
};

