function mostWordsFound(sentences: string[]): number {
    return Math.max(...sentences.map(sentence => Array.prototype.filter.call(sentence, l => l === ' ').length)) + 1;
};

