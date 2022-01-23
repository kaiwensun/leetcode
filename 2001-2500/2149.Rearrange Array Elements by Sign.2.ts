function rearrangeArray(nums: number[]): number[] {
    function * pick(sign: number) {
        for (let num of nums) {
            if (Math.sign(num) === sign) {
                yield num;
            }
        }
    }
    const pos = pick(1);
    const neg = pick(-1);
    const res: number[] = [];
    for (let i = 0; i < nums.length / 2; i++) {
        res.push(pos.next().value as number);
        res.push(neg.next().value as number);
    }
    return res;
};

