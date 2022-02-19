function isOneBitCharacter(bits: number[]): boolean {
    let i = bits.length - 1;
    while (bits[--i]);
    return !((bits.length - i) % 2);
};

