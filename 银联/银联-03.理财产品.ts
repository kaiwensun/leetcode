function maxInvestment(product: number[], limit: number): number {
    product.push(0);
    const stack = product.sort((a, b) => a - b).map(p => [p, 1]);
    const MOD = 1e9 + 7;
    let res = 0;
    while (limit && stack.length - 1) {
        if (stack[stack.length - 1][1] === 0) {
            stack.pop();
        }
        while (stack.length >= 2 && stack[stack.length - 1][0] == stack[stack.length - 2][0]) {
            const item = stack.pop();
            stack[stack.length - 1][1] += item[1];
        }
        const item = stack[stack.length - 1];
        if (stack.length == 1) {
            break;
        }
        if (item[1] >= limit) {
            res += (item[0] * limit) % MOD;
            res %= MOD;
            // item[1] -= limit;
            limit = 0;
        } else {
            const smallerPrice = stack[stack.length - 2][0];
            const priceDiff = item[0] - smallerPrice;
            if (priceDiff * item[1] <= limit) {
                res += (smallerPrice + 1 + item[0]) * priceDiff / 2 * item[1] % MOD;
                res %= MOD;
                item[0] = smallerPrice;
                limit -= item[1] * priceDiff;
            } else {
                const times = limit - limit % item[1];
                const priceDiff = times / item[1];
                res += (item[0] - priceDiff + 1 + item[0]) * priceDiff / 2 * item[1] % MOD;
                res %= MOD;
                item[0] -= priceDiff;
                limit -= item[1] * priceDiff;
            }
        }
    }
    return res;
};

