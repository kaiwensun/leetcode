function shortestCompletingWord(licensePlate: string, words: string[]): string {
    function count(word) {
        const counter = {}
        for (let c of word) {
            if ('a' <= c && c <= 'z') {
                counter[c] ||= 0;
                counter[c]++;
            }
        }
        return counter;
    }
    function completing(target, counter) {
        for (let key of Object.keys(target)) {
            if ((counter[key] || 0) < target[key]) {
                return false;
            }
        }
        return true;
    }
    const target = count(licensePlate.toLowerCase());
    let res = undefined
    for (let word of words) {
        if ((res?.length || Infinity) > word.length && completing(target, count(word))) {
            res = word;
        }
    }
    return res;
};

