function minimumMoves(s: string): number {
    let res = 0, i = 0;
    while (i < s.length) {
        if (s[i] === 'X') {
            i += 3;
            res++;
        } else {
            i += 1;
        }
    }
    return res;
};

