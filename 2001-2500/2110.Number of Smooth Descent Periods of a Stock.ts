function getDescentPeriods(prices: number[]): number {
    let prev = prices[0] - 1;
    let res = 0;
    let period = 0;
    for (let price of prices) {
        if (prev - 1 === price) {
            period++;
        } else {
            period = 1;
        }
        res += period;
        prev = price;
    }
    return res;
};

