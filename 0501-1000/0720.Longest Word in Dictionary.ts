function longestWord(words: string[]): string {
    words.sort();
    let res = "";
    const stack = [""];
    for (const word of words) {
        while (stack.length > word.length) {
            stack.pop();
        }
        if (stack.length !== word.length) {
            continue;
        }
        if (word.startsWith(stack[stack.length - 1])) {
            stack.push(word);
            if (word.length > res.length) {
                res = word;
            }
        }
    }
    return res;
};

