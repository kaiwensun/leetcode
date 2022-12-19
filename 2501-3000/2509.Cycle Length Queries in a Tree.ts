function cycleLengthQueries(n: number, queries: number[][]): number[] {
    return queries.map(([a, b]) => {
        let res = 0;
        while (a !== b) {
            if (a > b) {
                const tmp = a; a = b; b = tmp;
            }
            b >>= 1;
            res++;
        }
        return res + 1;
    });
};

