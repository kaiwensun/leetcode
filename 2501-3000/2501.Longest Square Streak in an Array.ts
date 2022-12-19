function longestSquareStreak(nums: number[]): number {
    function getBase(num: number) {
        while (Number.isInteger(Math.sqrt(num))) {
            num = Math.sqrt(num);
        }
        return num;
    }
    function getSize(base: number, group: Set<number>) {
        let res = 0, cur = 0;
        for (let num = base; num < MAX; num *= num) {
            if (group.has(num)) {
                cur++;
            } else {
                cur = 0;
            }
            res = Math.max(res, cur);
        }
        return res > 1 ? res : -1;
    }
    const MAX = 10 ** 5 + 1;
    const series: {[key: number]: Set<number>} = {};
    nums.forEach(num => {
        const base = getBase(num);
        series[base] ||= new Set<number>();
        series[base].add(num);
    });
    return Object.entries(series).reduce((acc, [base, group]) => Math.max(acc, getSize(parseInt(base), group)), -1);
};

