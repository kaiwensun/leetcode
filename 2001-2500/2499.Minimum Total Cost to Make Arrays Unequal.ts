function minimumTotalCost(nums1: number[], nums2: number[]): number {
    const sameIdx = nums1.map((_, i) => i).filter(i => nums1[i] === nums2[i]);
    let mostCommon: number = undefined;
    let frequency = 0;
    sameIdx.forEach(i => {
        if (frequency === 0) {
            mostCommon = nums1[i];
        }
        if (mostCommon === nums1[i]) {
            frequency++;
        } else {
            frequency--;          
        }
    });
    const mostCommonCnt = sameIdx.filter(i => nums1[i] === mostCommon).length;
    let remainingCnt = mostCommonCnt - (sameIdx.length - mostCommonCnt);
    let res = sameIdx.reduce((acc, i) => acc + i, 0);
    if (remainingCnt <= 0) {
        return res;
    }
    let sameIdxIter = 0;
    for (let i = 0; i < nums2.length && remainingCnt; i++) {
        if (sameIdxIter < sameIdx.length && sameIdx[sameIdxIter] === i) {
            sameIdxIter++;
            continue;
        }
        if (mostCommon === nums2[i] || mostCommon === nums1[i]) {
            continue;
        }
        remainingCnt--;
        res += i;
    }
    return remainingCnt ? -1 : res;
};

