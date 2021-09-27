const MOD = 10 ** 9 + 7;

function numDecodings(s: string): number {
    let ones = 1, tens = 0, twenties = 0;
    for (const c of s) {
        let newOnes, newTens, newTwenties;
        if (c == '0') {
            newOnes = tens + twenties;
            newTens = 0;
            newTwenties = 0;
        } else if (c == '*') {
            newOnes = (ones + tens) * 9 + twenties * 6;
            newTens = newTwenties = ones;
        } else if (c == '1') {
            newOnes = ones + tens + twenties;
            newTens = ones;
            newTwenties = 0;
        } else if (c == '2') {
            newOnes = ones + tens + twenties;
            newTens = 0;
            newTwenties = ones;
        } else if (c <= '6') {
            newOnes = ones + tens + twenties;
            newTens = newTwenties = 0;
        } else {
            newOnes = ones + tens;
            newTens = newTwenties = 0;
        }
        ones = newOnes % MOD;
        tens = newTens % MOD;
        twenties = newTwenties % MOD;
    }
    return ones;
};

