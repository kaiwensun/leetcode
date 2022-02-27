function prefixCount(words: string[], pref: string): number {
    return words.filter(word => word.startsWith(pref)).length;
};

