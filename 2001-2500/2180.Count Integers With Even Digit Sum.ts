function countEven(num: number): number {
    let cnt = 0;
    for (let i = 1; i <= num; i++) {
        if (("" + i).split('').map(d => parseInt(d)).reduce((a, b) => a + b, 0) % 2 === 0) {
            cnt++;
        }
    }
    return cnt;
};

