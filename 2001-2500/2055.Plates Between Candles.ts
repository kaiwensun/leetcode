function platesBetweenCandles(s: string, queries: number[][]): number[] {
    const prev = Array(s.length);
    const post = Array(s.length);
    const prefix_sum = Array(s.length);
    let last = -1;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '|') last = i;
        prev[i] = last;
    }
    last = s.length;
    for (let i = s.length - 1; i > -1; i--) {
        if (s[i] === '|') last = i;
        post[i] = last;
    }
    last = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '*') last++;
        prefix_sum[i] = last;
    }
    return queries.map(([left, right]) => {
        left = post[left];
        right = prev[right];
        return left >= right ? 0 : prefix_sum[right] - prefix_sum[left];
    })
};

