function reorderedPowerOf2(n: number): boolean {
    return squares.has(hash(n));
};

function hash(n: number) {
    const count = Array(10).fill(0);
    while (n) {
        count[n % 10] ++;
        n = ~~(n / 10);
    }
    return count.join('');
}

const squares = new Set();
for (let square = 1; square <= 10e9 && square > 0; square <<= 1) {
    squares.add(hash(square));
}


