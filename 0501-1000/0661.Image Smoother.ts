function imageSmoother(img: number[][]): number[][] {
    function smooth(i, j) {
        let sum = 0, cnt = 0;
        for (const x of [i - 1, i, i + 1]) {
            for (const y of [j - 1, j, j + 1]) {
                if (img[x]?.[y] !== undefined) {
                    sum += img[x][y];
                    cnt++;
                }
            }
        }
        return Math.floor(sum / cnt);
    }
    const res = [];
    for (let i = 0; i < img.length; i++) {
        res.push([]);
        for (let j = 0; j < img[i].length; j++) {
            res[i].push(smooth(i, j));
        }
    }
    return res;
};


