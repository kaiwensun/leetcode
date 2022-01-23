function countElements(nums: number[]): number {
    let mn = Infinity, mx = -Infinity, counter = {0:0}, res = 0;
    for (let num of nums) {
        mn = Math.min(mn, num);
        mx = Math.max(mx, num);
        counter[num] ||= 0;
        counter[num]++;
    }
    for (let [key, value] of Object.entries(counter)) {
        if (key === ''+mn || key === ''+mx) continue;
        res += value;
    }
    return res;
};

