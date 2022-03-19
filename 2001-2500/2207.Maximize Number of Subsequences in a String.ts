function maximumSubsequenceCount(text: string, pattern: string): number {
    let finalResult = 0;
    for (let i of [0, 1]) {
        let res = 0, count = i;
        for (let i = 0; i < text.length; i++) {
            if (text[i] === pattern[1]) {
                res += count;
            }
            if (text[i] === pattern[0]) {
                count++;
            }
        }
        if (i === 0) {
            res += count;
        }
        finalResult = Math.max(finalResult, res);
    }
    return finalResult;
};

