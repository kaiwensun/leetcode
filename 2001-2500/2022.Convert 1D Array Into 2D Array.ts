function construct2DArray(original: number[], m: number, n: number): number[][] {
    if (m * n !== original.length) {
        return [];
    }
    const result = [];
    for (let i = 0; i < original.length; i += n) {
        result.push(original.slice(i, i + n));
    }
    return result;
};

