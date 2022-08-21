function largestPalindromic(num: string): string {
    const cnt: {[key: string]: number} = {};
    [...num].forEach(c => {
        cnt[c] ||= 0;
        cnt[c]++;
    });
    let remain = "";
    const res: string[] = [];
    for (let c of "9876543210") {
        res.push(c.repeat((Math.floor(cnt[c] || 0) / 2)));
        if (remain === "" && (cnt[c] || 0) % 2 === 1) {
            remain = c;
        }
    }
    const first = res.join("");
    const second = res.reverse().join("");
    if (first[0] === "0") {
        return remain.length ? remain : "0";
    }
    return first + remain + second;
};

