function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const res: number[] = new Array(arr.length);
    for (let i = 0; i < arr.length; i++) {
        res[i] = fn(arr[i], i);
    }
    return res;
};

