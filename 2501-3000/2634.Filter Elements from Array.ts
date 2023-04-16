function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const res: any[] = [];
    arr.forEach((num, i) => {
        if (fn(num, i)) {
            res.push(num);
        }
    });
    return res;
};

