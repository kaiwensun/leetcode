function minMovesToMakePalindrome(s: string): number {
    const N = s.length;
    const array = s.split('');
    function choose(fixed1: number) {
        const fixed2 = N - 1 - fixed1;
        let p1 = fixed2, p2 = fixed1;
        while (array[p1] !== array[fixed1]) {
            p1--;
        }
        while (array[p2] !== array[fixed2]) {
            p2++;
        }
        return [fixed2 - p1, p2 - fixed1];
    }
    function move(from, to) {
        if (from === to) {
            return;
        }
        const dir = from < to ? 1 : -1;
        let p = from;
        let char = array[from];
        while (p !== to) {
            array[p] = array[p + dir];
            p += dir;
        }
        array[p] = char;
    }
    let res = 0;
    for (let i = 0; i < N / 2; i++) {
        const [size1, size2] = choose(i);
        if (size1 < size2) {
            res += size1;
            move(N - 1 - i - size1, N - 1 - i);
        } else {
            res += size2;
            move(i + size2, i);
        }
    }
    return res;
};

