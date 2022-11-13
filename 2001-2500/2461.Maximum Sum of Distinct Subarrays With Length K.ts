function maximumSubarraySum(nums: number[], k: number): number {
    const counter = {};
    let countDups = 0, sum = 0, res = 0;
    nums.forEach((num, i) => {
        sum += num;
        counter[num] ||= 0; counter[num]++;
        if (counter[num] === 2) {
            countDups++;
        }
        if (i >= k) {
            const prev = nums[i - k]
            counter[prev]--;
            sum -= prev;
            if (counter[prev] === 1) {
                countDups--;
            }
        }
        if (i >= k - 1 && countDups === 0) {
            res = Math.max(res, sum);
        }
    });
    return res;
};

