function removeStars(s: string): string {
    const res: string[] = [];
    let cnt = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === '*') {
            cnt ++;
        } else {
            if (cnt) {
                cnt--;
            } else {
                res.push(s[i]);
            }
        }
    }
    return res.reverse().join("");
};

