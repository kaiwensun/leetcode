function shortestSequence(rolls: number[], k: number): number {
    function findAll(start) {
        const seen = new Array(k);
        let seenCnt = 0;
        for (let i = start; i >= 0; i--) {
            if (!seen[rolls[i]]) {
                seen[rolls[i]] = true;
                seenCnt++;
                if (seenCnt === k) {
                    return i;
                }
            }
        }
        return -1;
    }

    let res = 0, i = rolls.length;
    while (i >= 0) {
        res++;
        i = findAll(i - 1);
    }
    return res;
};

