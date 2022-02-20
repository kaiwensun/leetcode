function coutPairs(nums: number[], k: number): number {
    const cnt = {};
    for (const num of nums) {
        const key = (num - 1) % k + 1;
        cnt[key] ||= 0;
        cnt[key]++;
    }
    let res = 0;
    for (let numStr of Object.keys(cnt)) {
        const num = parseInt(numStr);
        let need = k / gcd(k, num);
        for (let partner = need; partner <= k; partner += need) {
            if (!cnt.hasOwnProperty(partner)) {
                continue;
            }
            res += cnt[num] * (num === partner ? cnt[partner] - 1 : cnt[partner]);
        }
    }
    return res / 2;
};

function gcd(a, b) {
    // assume a >= b
    while (b) {
        const tmp = a % b;
        a = b;
        b = tmp;
    }
    return a;
}


