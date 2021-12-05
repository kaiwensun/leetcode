function findEvenNumbers(digits: number[]): number[] {
    const LENGTH = 3;
    const counter = {};
    const res = [];
    for (let digit of digits) {
        counter[digit] ||= 0;
        counter[digit]++;
    }
    function dfs(i, cur) {
        if (i === LENGTH) {
            res.push(cur)
            return;
        }
        cur *= 10
        const start = i === 0 ? 1 : 0;
        const delta = i === LENGTH - 1 ? 2 : 1;
        for (let d = start; d < 10; d += delta) {
            if (counter[d]) {
                counter[d]--;
                dfs(i + 1, cur + d);
                counter[d]++;
            }
        }
    }
    dfs(0, 0);
    return res;
};

