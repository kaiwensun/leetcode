function hardestWorker(n: number, logs: number[][]): number {
    let res = [-1, -1];
    let cur = 0;
    for (const log of logs) {
        const duration = log[1] - cur;
        if (duration > res[0]) {
            res = [duration, log[0]];
        } else if (duration == res[0] && log[0] < res[1]) {
            res = [duration, log[0]];
        }
        cur = log[1];
    }
    return res[1];
};

