function garbageCollection(garbage: string[], travel: number[]): number {
    const acc = garbage.reduce((acc, s, i) =>
        {[...s].forEach(c => {acc.cnt[c]++; acc.lastSeen[c] = i}); return acc},
        {'cnt': {'M': 0, 'P': 0, 'G': 0}, lastSeen: {'M': 0, 'P': 0, 'G': 0}});
    travel.forEach((t, i) => travel[i] += travel[i - 1] || 0);
    travel[-1] = 0;
    return [..."MPG"].map(c => acc.cnt[c] + travel[acc.lastSeen[c] - 1]).reduce((sum, num) => sum + num, 0);
};

