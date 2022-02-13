function minimumRemoval(beans: number[]): number {
    const cnt = {};
    for (const bean of beans) {
        cnt[bean] ||= 0;
        cnt[bean]++;
    }
    const keys = Object.keys(cnt).sort((a, b) => parseInt(a) - parseInt(b));
    const total = beans.reduce((acc, bean) => acc + bean, 0);
    let res = total;
    let lCnt = 0;
    for (const key of keys) {
        res = Math.min(res, total - (beans.length - lCnt) * parseInt(key));
        lCnt += cnt[key];
    }
    return res;
};

