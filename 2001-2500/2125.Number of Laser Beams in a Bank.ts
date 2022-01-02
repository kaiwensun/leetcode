function numberOfBeams(bank: string[]): number {
    let res = 0, prev = 0;
    for (const row of bank) {
        const cnt = [].filter.call(row, c => c == '1') .length;
        if (cnt) {
            res += prev * cnt;
            prev = cnt;
        }
    }
    return res;
};

