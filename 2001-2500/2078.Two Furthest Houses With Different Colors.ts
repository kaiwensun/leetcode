function maxDistance(colors: number[]): number {
    const n = colors.length;
    for (let i = 0; i < n - 1; i++) {
        if (colors[i] !== colors[n - 1] || colors[n - 1 - i] !== colors[0]) {
            return n - 1 - i;
        }
    }
    return -1;
};

