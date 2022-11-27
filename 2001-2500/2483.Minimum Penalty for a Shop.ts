function bestClosingTime(customers: string): number {
    let closeCost = [...customers].reduce((acc, c) => acc + Number(c === "Y"), 0);
    let openCost = 0;
    let closeTime = -1;
    [...customers].reduce((minCost, c, i) => {
        closeCost -= Number(c === "Y");
        openCost += Number(c === "N");
        if (minCost > closeCost + openCost) {
            minCost = closeCost + openCost;
            closeTime = i;
        }
        return Math.min(minCost, closeCost + openCost);
    }, closeCost + openCost);
    return closeTime + 1;
};

