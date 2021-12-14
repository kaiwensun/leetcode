function minimumRefill(plants: number[], capacityA: number, capacityB: number): number {
    let a = capacityA, b = capacityB;
    let i = 0, j = plants.length - 1;
    let res = 0;
    while (i < j) {
        if (plants[i] > a) {
            res++;
            a = capacityA;
        }
        if (plants[j] > b) {
            res++;
            b = capacityB;
        }
        a -= plants[i++];
        b -= plants[j--];
    }
    if (i === j && plants[i] > Math.max(a, b)) {
        res++;
    }
    return res;
};

