function minimizedMaximum(n: number, quantities: number[]): number {
    function test(mx) {
        let i = 0;
        let q = 0;
        let quantity = 0;
        for (let i = 0; i < n; i++) {
            if (quantity <= 0) {
                if (q === quantities.length) {
                    return true;
                }
                quantity = quantities[q++];
            }
            quantity -= mx;
        }
        return q === quantities.length && quantity <= 0;
    }
    const sum = quantities.reduce((acc, num) => acc + num, 0);
    let l = Math.ceil(sum / n), r = sum + 1;
    while (l < r) {
        const mid = (l + r) >> 1;
        if (test(mid)) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }
    return l;
    
};

