function minimumBuckets(street: string): number {
    const cnt = { 'H': 0, '.': 0 };
    let last = -2, res = 0;
    for (let i = 0; i < street.length; i++) {
        cnt[street[i]]++;
        if (street[i] === 'H') {
            if (![street[i - 1], street[i + 1]].includes('.')) return -1;
            if (last === i - 1) continue;
            last = street[i + 1] === '.' ? i + 1 : i - 1;
            res++;
        }
    }
    return last === -2 && cnt.H ? -1 : res;
};

