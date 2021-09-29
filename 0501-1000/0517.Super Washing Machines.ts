function findMinMoves(machines: number[]): number {
    let sum = 0;
    for (let machine of machines) {
        sum += machine;
    }
    if (sum % machines.length) {
        return -1;
    }
    const avg = sum / machines.length;
    let budget = 0, prev_budget = 0, res = 0;
    for (let machine of machines) {
        budget += machine - avg;
        const donate = prev_budget < 0 && budget > 0 ? budget - prev_budget : Math.abs(budget);
        res = Math.max(res, donate);
        prev_budget = budget;
    }
    return res;
};

