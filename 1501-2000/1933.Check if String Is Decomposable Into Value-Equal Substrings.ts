function isDecomposable(s: string): boolean {
    let prev = '', cnt = 0, tolerated = false;
    for (let c of s + '#') {
        if (c === prev) {
            cnt ++;
        } else {
            if (cnt % 3 !== 0) {
                if (!tolerated && cnt % 3 == 2) {
                    tolerated = true;
                } else {
                    return false;
                }
            }
            cnt = 1;
        }
        prev = c;
    }
    return tolerated;
};

