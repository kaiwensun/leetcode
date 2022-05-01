function minimumCardPickup(cards: number[]): number {
    const seen = {};
    let res = Infinity;
    cards.forEach((num, i) => {
        if (seen[num] !== undefined) {
            res = Math.min(res, i - seen[num])
        }
        seen[num] = i;
    });
    return Infinity === res ? -1 : res + 1;
};

