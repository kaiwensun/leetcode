function reorderedPowerOf2(n: number): boolean {
    return squares.has(hash(n));
};

function hash(n: number) {
    return ('' + n).split('').sort().join('');
}

const squares = new Set();
for (let square = 1; square <= 10e9 && square > 0; square <<= 1) {
    squares.add(hash(square));
}

