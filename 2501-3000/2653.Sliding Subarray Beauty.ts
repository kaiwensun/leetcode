function getSubarrayBeauty(nums: number[], k: number, x: number): number[] {
    const OFFSET = 50;
    function get(x) {
        let count = 0;
        for (let i = 0; i < counter.length; i++) {
            count += counter[i];
            if (count >= x) {
                return Math.min(0, i - OFFSET);
            }
        }
        throw new Error(`unable to get ${x} smallest from ${JSON.stringify(counter)}`);
    }
    const counter = new Array(101).fill(0);
    const res: number[] = [];
    for (let i = 0; i < nums.length; i++) {
        counter[OFFSET + nums[i]]++;
        if (i >= k) {
            counter[OFFSET + nums[i - k]]--;
        }
        if (i >= k - 1) {
            res.push(get(x));
        }
    }
    return res;
};

