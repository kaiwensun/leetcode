function stoneGameIX(stones: number[]): boolean {
    const cnt = [0, 0, 0];
    
    for (const stone of stones) {
        cnt[stone % 3]++;
    }
    if (cnt[0] % 2) {
        return Math.abs(cnt[1] - cnt[2]) > 2;
    }
    return Math.min(cnt[1], cnt[2]) >= 1;
};

