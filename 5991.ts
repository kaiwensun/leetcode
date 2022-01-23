function rearrangeArray(nums: number[]): number[] {
    function pick(sign: number) {
        return nums.filter(num => Math.sign(num) === sign);
    }
    const pos = pick(1);
    const neg = pick(-1);
    const res: number[] = [];
    for (let i = 0; i < pos.length; i++) {
        res.push(pos[i]);
        res.push(neg[i]);
    }
    return res;
};

