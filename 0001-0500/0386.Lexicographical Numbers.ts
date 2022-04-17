function lexicalOrder(n: number): number[] {
    const res = new Array(n);
    let state = 1;
    for (let i = 0; i < n; i++) {
        res[i] = state;
        if (state * 10 <= n) {
            state *= 10;
        } else {
            while (state % 10 === 9 || state + 1 > n) {
                state = Math.floor(state / 10);
            }
            state++;
        }
    }
    return res;
};

