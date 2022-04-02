function nextGreatestLetter(letters: string[], target: string): string {
    const targetCode = target.charCodeAt(0);
    let res = Infinity;
    for (const letter of letters) {
        const code = letter.charCodeAt(0);
        for (const value of [code, code + 26]) {
            if (value > targetCode) {
                res = Math.min(res, value);
            }
        }
    }
    if (res > 'z'.charCodeAt(0)) {
        res -= 26;
    }
    return String.fromCharCode(res);
};

