function maxConsecutiveAnswers(answerKey: string, k: number): number {
    let l = 0, res = 0, r = 0;
    const cnt = {T: 0, F: 0};
    while (r < answerKey.length) {
        cnt[answerKey[r++]] += 1;
        while (Math.min(cnt.T, cnt.F) > k) {
            cnt[answerKey[l++]]--;
        }
        res = Math.max(res, r - l);
    }
    return res;
};

