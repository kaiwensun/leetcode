function kthDistinct(arr: string[], k: number): string {
    const cnt = {};
    arr.forEach(word => {
        cnt[word] ||= 0;
        cnt[word]++;
    });
    for (let word of arr) {
        if (cnt[word] === 1) {
            if (--k == 0) {
                return word;
            }
        }
    }
    return "";
};

