function distributeCandies(candyType: number[]): number {
    return Math.min(new Set(candyType).size, candyType.length / 2);
};

