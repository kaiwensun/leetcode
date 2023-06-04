function findThePrefixCommonArray(A: number[], B: number[]): number[] {
    const N = A.length;
    const a = new Array(N).fill(false);
    const b = new Array(N).fill(false);
    let cnt = 0;
    const res = [];
    for (let i = 0; i < N; i++) {
        if (b[A[i] - 1]) cnt++;
        a[A[i] - 1] = true;
        if (a[B[i] - 1]) cnt++;
        b[B[i] - 1] = true;
        res.push(cnt);
    }
    return res;
};

