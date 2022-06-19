const dp = {};
function minimumNumbers(num: number, k: number): number {
    if (num === 0) {
        return 0;
    }
    if (k === 0) {
        return num % 10 === 0 ? 1 : -1;
    }
    let res = 1;
    while (res * k <= num) {
        if ((num - res * k) % 10 === 0) {
            return res;
        }
        res++;
    }
    return -1;
};

