function maximumWhiteTiles(tiles: number[][], carpetLen: number): number {
    const N = tiles.length;
    tiles.sort((a, b) => a[0] - b[0]);
    tiles.push([Infinity, Infinity]);
    let q = 0, res = 0, covered = 0;
    for (let p = 0; p < N; p++) {
        while (tiles[p][0] + carpetLen > tiles[q][1]) {
            covered += tiles[q][1] - tiles[q][0] + 1;
            q++;
        }
        const partiallyCovered = Math.max(0, tiles[p][0] + carpetLen - tiles[q][0]);
        res = Math.max(res, covered + partiallyCovered);
        covered -= tiles[p][1] - tiles[p][0] + 1;
    }
    return res;
};

