function minimumCost(cost: number[]): number {
    function * pay() {
        let tick = true;
        for (let i = 0; i < cost.length; i++) {
            const price = cost[i];
            if (price) {
                tick = !tick;
                if (tick) {
                    yield i;
                }
            }
        }
    }

    cost.sort((a, b) => b - a);
    const payIter = pay();
    let j = payIter.next().value as number;
    for (let i = 2; i < cost.length; i++) {
        i = Math.max(j + 1, i);
        if (cost[i] <= cost[j]) {
            cost[i] = 0;
            j = payIter.next().value as number;
        }
    }
    return cost.reduce((acc, num) => acc + num, 0);
};

