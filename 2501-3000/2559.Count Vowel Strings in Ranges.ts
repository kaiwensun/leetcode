function vowelStrings(words: string[], queries: number[][]): number[] {
    const prefix = [0]
    words.forEach((word, i) => {
        prefix.push(('aeiou'.includes(word[0]) && 'aeiou'.includes(word[word.length - 1]) ? 1 : 0) + prefix[i]);
    });
    return queries.map(q => prefix[q[1] + 1] - prefix[q[0]]);
};

