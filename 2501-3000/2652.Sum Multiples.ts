const prefix = new Array(1001);
prefix[0] = 0;
for (let i = 1; i < prefix.length; i++) {
    prefix[i] = prefix[i - 1];
    if (!(i % 3 && i % 5 && i % 7)) {
        prefix[i] += i;
    }
}
function sumOfMultiples(n: number): number {
    return prefix[n];
};


