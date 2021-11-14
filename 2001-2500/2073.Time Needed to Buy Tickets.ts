function timeRequiredToBuy(tickets: number[], k: number): number {
    let res = 0;
    tickets.forEach((ticket, i) => {
        res += Math.min(tickets[k] - (i <= k ? 0 : 1), ticket);;
    });
    return res;
};

