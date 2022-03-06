function minMovesToMakePalindrome(s: string): number {
    const N = s.length;
    const array = s.split('');
    let res = 0;
    let mid = 0;
    for (let l = 0; l < (N - 1) / 2; l++) {
        let r = N - 1 - l - mid;
        const target = array[l];
        let tmp = undefined, fly = array[r];
        while (target !== fly) {
            tmp = array[r - 1];
            array[r - 1] = fly;
            fly = tmp;
            r--;
        }
        // array[N - 1 - l - mid] = fly; // not necessary
        if (r === l) {
            mid = 1;
            res += (N - 1 - mid) / 2 - r;
            l--;
        } else {
            res += N - 1 - l - mid - r;
        }
    }
    return res;
};

