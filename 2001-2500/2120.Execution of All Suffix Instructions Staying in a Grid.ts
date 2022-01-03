function executeInstructions(n: number, startPos: number[], s: string): number[] {
    const DELTA = {
        'D': [1, 0],
        'U': [-1, 0],
        'L': [0, -1],
        'R': [0, 1]
    }
    function simulate(start: number) {
        let [x, y] = startPos;
        for (let i = start; i < s.length; i++) {
            x += DELTA[s[i]][0];
            y += DELTA[s[i]][1];
            if (!(0 <= x && x < n && 0 <= y && y < n)) {
                return i - start;
            }
        }
        return s.length - start;
    }
    const res = Array(s.length);
    for (let i = 0; i < s.length; i++) {
        res[i] = simulate(i);
    }
    return res;
};

