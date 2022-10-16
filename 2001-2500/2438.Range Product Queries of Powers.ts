const MOD = 10 ** 9 + 7;

function productQueries(n: number, queries: number[][]): number[] {
    const power = [];
    while (n) {
        const bit = ((n ^ (n - 1)) + 1) >> 1;
        power.push(bit);
        n -= bit;
    }
    return queries.map(query => {
        let answer = 1;
        for (let i = query[0]; i <= query[1]; i++) {
            answer *= power[i];
            answer %= MOD;
        }
        return answer;
    });
};

