function convertToBase7(num: number): string {
    const sign = num >= 0 ? "" : "-";
    num = Math.abs(num);
    const res = [];
    while (num) {
        res.unshift(num % 7);
        num = Math.floor(num / 7);
    }
    if (!res.length) {
        res.unshift(0);
    }
    res.unshift(sign);
    return res.join("");
};

