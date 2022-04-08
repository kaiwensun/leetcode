function reachingPoints(sx: number, sy: number, tx: number, ty: number): boolean {
    if (sx == ty && sy == tx) return sx == sy;
    [sx, sy] = [sx, sy].sort((a, b) => a - b);
    [tx, ty] = [tx, ty].sort((a, b) => a - b);
    while (sy < ty && tx < ty) {
        const diff = Math.floor((ty - sy) / tx) * tx ||
            Math.floor((ty - sx) / tx) * tx ||
            1;
        [tx, ty] = [ty - diff, tx].sort((a, b) => a - b);
    }
    return sx == tx && sy == ty;
};

