function subarrayLCM(nums: number[], k: number): number {

    function gcd(a, b) {
        if (a > b) {
            const tmp = a; a = b; b = tmp;
        }
        while (a) {
            b %= a;
            const tmp = a; a = b; b = tmp;
        }
        return b;
    }
    function scm(a, b) {
        return a * b / gcd(a, b);
    }

    let res = 0;
    for (let i = 0; i < nums.length; i++) {
        let m = nums[i];
        for (let j = i; j < nums.length; j++) {
            m = scm(m, nums[j]);
            if (m === k) {
                res++;
            }
        }
    }
    return res;
};

