function numberOfWays(corridor: string): number {
    const MOD = 1e9 + 7;
    let seatCnt = 0, res = 1, consecPlant = 0;
    for (let c of corridor) {
        if (c === 'S') {
            seatCnt++;
        }
        if (seatCnt % 2) {
            if (c === 'S' && seatCnt > 1) {
                res *= (consecPlant + 1);
                res %= MOD;
            }
        } else {
            if (c === 'P') {
                consecPlant++;
            }
        }
        if (seatCnt & 1) {
            consecPlant = 0;
        }
    }
    return (seatCnt % 2 || seatCnt < 2) ? 0 : res;
};

