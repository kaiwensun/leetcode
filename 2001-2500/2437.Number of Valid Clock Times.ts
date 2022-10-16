function countTime(time: string): number {
    let res = 1;
    const h = time.substr(0, 2);
    const m = time.substr(3, 2);
    if (h === '??') {
        res = 24;
    } else if (h[1] === '?') {
        res = h[0] === '2' ? 4 : 10;
    } else if (h[0] === '?'){
        res = h[1] < '4' ? 3 : 2;
    }
    if (m[0] === '?') {
        res *= 6;
    }
    if (m[1] === '?') {
        res *= 10;
    }
    return res;
};

