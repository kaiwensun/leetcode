function similarPairs(words: string[]): number {
    const group: {[key: number] : number} = {};
    words.forEach(word => {
        const hash = [...word].map(c => 1 << c.codePointAt(0)).reduce((acc, bit) => acc | bit, 0);
        group[hash] ||= 0;
        group[hash]++;
    });
    return Object.values(group).reduce((acc, cnt) => acc + cnt * (cnt - 1) / 2, 0);
};

