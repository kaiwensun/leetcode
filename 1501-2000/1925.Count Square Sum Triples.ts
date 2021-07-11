function countTriples(n: number): number {
    const n2 = n * n;
    const squares = new Set();
    let res = 0;
    for (let i = 1; i <= n; i++) {
        squares.add(i * i);
    }
    for (let a = 1; a < n; a++) {
        const a2 = a * a;
        let b2 = a2;
        for (let b = a; b < n; b++) {
            if (a2 + b2 > n2) {
                break;
            }
            if (squares.has(a2 + b2)) {
                res += a == b ? 1 : 2;
            }
            b2 += b + b + 1;
        }
    }
    return res;
};

