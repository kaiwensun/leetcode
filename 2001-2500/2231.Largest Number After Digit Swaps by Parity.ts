function largestInteger(num: number): number {
    const cnt = new Array(10).fill(0);
    [...("" + num)].forEach(d => cnt[d]++);
    const res = [];
    for (const digit of [...("" + num)]) {
        const newDigits = "97531".includes(digit) ? "97531" : "86420";
        for (const newDigit of newDigits) {
            if (cnt[newDigit]) {
                cnt[newDigit]--;
                res.push(newDigit);
                break;
            }
        }
    }
    return parseInt(res.join(""));
};

