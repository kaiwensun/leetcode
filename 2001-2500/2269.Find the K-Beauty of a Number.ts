function divisorSubstrings(num: number, k: number): number {
    const mask = 10 ** k;
    let res = 0;
    let scanner = num;
    while (scanner >= mask / 10) {
        const divider = scanner % mask;
        if (num % divider === 0) {
            res++;
        }
        scanner  = Math.floor(scanner / 10);
    }
    return res;
};

