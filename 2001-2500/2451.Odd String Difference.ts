function oddString(words: string[]): string {
    function diff(i, j) {
        return words[i][j].charCodeAt(0) - words[i][j + 1].charCodeAt(0);
    }
    for (let j = 0; j < words[0].length - 1; j++) {
        const diff0 = diff(0, j);
        if (diff0 !== diff(1, j) && diff0 !== diff(2, j)) {
            return words[0];
        }
        for (let i = 1; i < words.length; i++) {
            if (diff0 !== diff(i, j)) return words[i];
        }
    }
};

