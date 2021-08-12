function canBeTypedWords(text: string, brokenLetters: string): number {
    const broken = new Set(brokenLetters);
    return text.split(" ").filter(word => ![].some.call(word, broken.has.bind(broken))).length;
};

