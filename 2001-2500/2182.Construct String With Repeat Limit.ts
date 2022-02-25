function repeatLimitedString(s: string, repeatLimit: number): string {
    const cnt = {};
    for (let i = 0; i < s.length; i++) {
        cnt[s[i]] ||= 0;
        cnt[s[i]]++;
    }
    let repeat = 0;
    const res = [];
    while (true) {
        let useLetter = undefined;
        for (let i = 25; i >= 0 && !useLetter; i--) {
            const letter = String.fromCharCode(97 + i);
            if (!cnt[letter]) continue;
            if (repeat === repeatLimit && res[res.length - 1] === letter) {
                continue;
            }
            useLetter = letter;
        }
        if (!useLetter) break;
        if (res.length && res[res.length - 1] != useLetter) {
            repeat = 1;
        } else {
            repeat++;
        }
        cnt[useLetter]--;
        res.push(useLetter);
    }
    return res.join('');
};

