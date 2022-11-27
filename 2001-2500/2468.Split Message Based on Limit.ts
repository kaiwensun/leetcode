function splitMessage(message: string, limit: number): string[] {
    if (limit <= 5) return [];
    function getArrayLen(digit: number) {
        let remainLetters = message.length;
        let arrLen = 0;
        for (let i = 1; i <= digit && remainLetters > 0; i++) {
            const letters = limit - 3 - digit - i;
            if (letters <= 0) break;
            const times = Math.min(10 ** i - 10 ** (i - 1), Math.ceil(remainLetters / letters));
            remainLetters -= letters * times;
            arrLen += times;
        }
        return remainLetters > 0 ? Infinity : arrLen;
    }
    function constructArray(arrLen: number) {
        const res = [];
        let start = 0;
        const digit = ('' + arrLen).length;
        for (let i = 1; i <= arrLen; i++) {
            const letters = limit - 3 - digit - ('' + i).length;
            res.push(`${message.substr(start, letters)}<${i}/${arrLen}>`);
            start += letters;
        }
        return res;
    }

    let shortestLen = Infinity;
    let bestDigit = 0;
    for (let digit = 1; digit < 6; digit++) {
        const arrLen = getArrayLen(digit);
        if (shortestLen > arrLen) {
            shortestLen = arrLen;
            bestDigit = digit;
        }
    }
    if (bestDigit === 0) return [];
    return constructArray(shortestLen);
};

