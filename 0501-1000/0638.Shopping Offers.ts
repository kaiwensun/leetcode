function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    let mn = Infinity;
    const N = price.length;
    function retail(needs: number[]) {
        let res = 0;
        needs.forEach((need, i) => {
            res += need * price[i];
        });
        return res;
    }
    function supply(needs: number[], special: number[]) {
        return Math.min(...(needs.map((need, i) => {
            return special[i] ? Math.floor(need / special[i]) : Infinity;
        })));
    }
    function dfs(needs: number[], i: number, cur: number) {
        if (cur >= mn) {
            return;
        }
        if (needs.every(n => !n)) {
            mn = cur;
            return;
        }
        if (i === special.length) {
            mn = Math.min(mn, cur + retail(needs));
            return;
        }
        const loop = supply(needs, special[i].slice(0, N));
        for (let j = 0; j <= loop; j++) {
            dfs(needs.map((need, k) => need - special[i][k] * j), i + 1, cur + special[i][N] * j);
        }
    }
    dfs(needs, 0, 0);
    return mn;
};

