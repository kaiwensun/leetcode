function findNthDigit(n: number): number {
    let length = 1;
    let search = 10;
    while (n >= search * length) {
        n += search;
        length++;
        search *= 10;
    }
    let i = Math.floor(n / length);
    let j = n % length;
    return parseInt(('' + i)[j]);
};

