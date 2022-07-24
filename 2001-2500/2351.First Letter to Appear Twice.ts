function repeatedCharacter(s: string): string {
    const seen = {};
    for (let c of [...s]) {
        if (seen[c]) return c;
        seen[c] = true;
    }
}

