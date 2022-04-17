function isStrobogrammatic(num: string): boolean {
    const pair = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6",
    }
    const same = "018";
    let i = 0, j = num.length - 1;
    while (i < j) {
        if (pair[num[i++]] !== num[j--]) {
            return false;
        }
    }
    return i !== j || same.includes(num[i]);
};

