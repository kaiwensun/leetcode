function doesValidArrayExist(derived: number[]): boolean {
    return derived.reduce((xor, num) => num ^ xor, 0) === 0;
};

