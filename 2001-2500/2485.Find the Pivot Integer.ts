function pivotInteger(n: number): number {
    let sum = 0;
    const total = (1 + n) * n / 2;
    for (let i = 1; i <= n; i++) {
        sum += i;
        if (sum === total - sum + i) return i;
        if (sum > total - sum + i) return -1;
    }
    return -1;
};

