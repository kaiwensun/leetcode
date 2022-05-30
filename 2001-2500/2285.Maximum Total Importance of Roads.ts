function maximumImportance(n: number, roads: number[][]): number {
    const cnt: {[k : string] : number} = {};
    roads.forEach(([a, b]) => {
        cnt[a] ||= 0; cnt[b] ||= 0;
        cnt[a]++; cnt[b]++;
    });
    return Object.values(cnt)
        .sort((a, b) => b - a)
        .map((value, i) => value * (n - i))
        .reduce((acc, x) => acc + x, 0);
};

