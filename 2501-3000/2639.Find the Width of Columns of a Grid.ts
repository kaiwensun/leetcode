function findColumnWidth(grid: number[][]): number[] {
    const res: number[] = [];
    grid.forEach(row => {
        row.forEach((ele, i) => {
            if (res.length === i) res.push(0);
            res[i] = Math.max(res[i], `${ele}`.length);
        });
    });
    return res;
};

