const everything = new Set();
for (let i = 0; i < 100000; i++) {
    const j = parseInt([...(i + '')].reverse().join(''));
    everything.add(i + j);
}

function sumOfNumberAndReverse(num: number): boolean {
    return everything.has(num);
};

