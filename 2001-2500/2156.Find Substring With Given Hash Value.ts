function subStrHash(s: string, power: number, modulo: number, k: number, hashValue: number): string {
    let hash = 0n, index = s.length;
    const hashValueBI = BigInt(hashValue);
    const moduloBI = BigInt(modulo);
    const powerBI = BigInt(power) % moduloBI;
    let powerKBI = BigInt(1);
    for (let i = 0; i < k; i++) {
        powerKBI = powerKBI * powerBI % moduloBI;
    }
    for (let i = s.length - 1; i >= 0; i--) {
        const val = BigInt(s.charCodeAt(i) - 96);
        hash = hash * powerBI % moduloBI + val;
        if (i + k < s.length) {
            const delVal = BigInt(s.charCodeAt(i + k) - 96);
            hash = hash - powerKBI * delVal % moduloBI;
            hash = (hash + moduloBI) % moduloBI;
        }
        hash %= moduloBI;
        if (hash == hashValueBI) {
            index = i;
        }
    }
    return s.substr(index, k);
};

