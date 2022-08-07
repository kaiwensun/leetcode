function mergeSimilarItems(items1: number[][], items2: number[][]): number[][] {
    const vw: {[n: number]: number} = {};
    [items1, items2].forEach(items => {
        items.forEach(([v, w]) => {
            vw[v] = (vw[v] || 0) + w;
        });
    });
    return Object.entries(vw).map(item => [parseInt(item[0]), item[1]]).sort((a, b) => a[0] - b[0]);
};

