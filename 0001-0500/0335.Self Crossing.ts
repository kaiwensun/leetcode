function isSelfCrossing(distance: number[]): boolean {
    function crossing(...[p0, p1, p2, p3]:number[][]) {
        if (!(p0 && p1 && p2 && p3)) {
            return false;
        }
        if (p2[1] === p3[1]) {
            let tmp = p2; p2 = p0; p0 = tmp;
            tmp = p3; p3 = p1; p1 = tmp;
        }
        return Math.min(p2[1], p3[1]) <= p0[1] && p0[1] <= Math.max(p2[1], p3[1]) && Math.min(p0[0], p1[0]) <= p2[0] && p2[0] <= Math.max(p0[0], p1[0]);
    }

    const history: number[][] = [null, null, null, null, [0, 0], [0, 0]];
    let p = [0, 0];
    const DIR = [[0, 1], [-1, 0], [0, -1], [1, 0]];
    for (let i = 0; i < distance.length; i++) {
        const dist = distance[i];
        p = [p[0] + dist * DIR[i % 4][0], p[1] + dist * DIR[i % 4][1]];
        history.push(p);
        if (crossing(history[0], history[1], history[5], history[6])) {
            return true;
        }
        if (crossing(history[2], history[3], history[5], history[6])) {
            return true;
        }
        history.shift();
    }
    return false;
};

