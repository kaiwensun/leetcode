function matchReplacement(s: string, sub: string, mappings: string[][]): boolean {
    const dict = {};
    for (const [f, t] of mappings) {
        dict[f] ||= [f];
        dict[f].push(t);
    }
    for (let i = 0; i <= s.length - sub.length; i++) {
        let res = true;
        for (let j = 0; j < sub.length; j++) {
            let ok = false;
            for (let matcher of (dict[sub[j]] || [sub[j]])) {
                if (s[i + j] === matcher) {
                    ok = true;
                    break;
                }
            }
            if (!ok) {
                res = false;
                break;
            }
        }
        if (res) {
            return true;
        }
    }
    return false;
};

