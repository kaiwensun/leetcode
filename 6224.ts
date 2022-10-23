function subarrayGCD(nums: number[], k: number): number {
    function gcd(a: number, b: number) {
        if (a < b) {const tmp = a; a = b; b = tmp;}
        while (b) {
            a %= b;
            const tmp = a; a = b; b = tmp;
        }
        return a;
    }
    let res = 0;
    for (let start = 0; start < nums.length; start++) {
        let cur = nums[start];
        for (let end = start; end < nums.length; end++) {
            cur = gcd(nums[end], cur);
            if (cur === k) res++;
        }
    }
    return res;
};

