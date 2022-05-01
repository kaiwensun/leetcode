function countPrefixes(words: string[], s: string): number {
    return words.filter(word => s.startsWith(word)).length;
};

