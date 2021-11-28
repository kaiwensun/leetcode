function countWords(words1: string[], words2: string[]): number {
    const counter = {};
    [words1, words2].forEach((words, i) => {
        words.forEach(word => {
            counter[word] ||= [0, 0];
            counter[word][i] ++;
        })
    })
    return Object.values(counter).filter(pair => pair[0] === 1 && pair[1] === 1).length;
};

