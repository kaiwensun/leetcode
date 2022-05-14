function largestTriangleArea(points: number[][]): number {
    const N = points.length;
    let res = 0;
    for (let i = 0; i < N; i++) {
        for (let j = i + 1; j < N; j++) {
            for (let k = j + 1; k < N; k++) {
                const p = [i, j, k].map(t => points[t]);
                let sm = 0;
                for (let t = 0; t < 3; t++) {
                    sm += p[t][0] * p[(t + 1) % 3][1] - p[t][0] * p[(t + 2) % 3][1];
                }
                res = Math.max(res, Math.abs(sm) / 2);
            }
        }
    }
    return res;
};

