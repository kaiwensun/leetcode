function goodTriplets(nums1: number[], nums2: number[]): number {
    const N = nums1.length;
    const segTree = Array(N * 2).fill(0);
    function add(index: number, segTree:number[]) {
        index += N;
        while (index) {
            segTree[index]++;
            index >>= 1;
        }
    }
    function query(start, end, segTree: number[]) {
        start += N;
        end += N;
        let res = 0;
        while (start < end) {
            if (start & 1) {
                res += segTree[start++];
            }
            if (end & 1) {
                res += segTree[--end]
            }
            start >>= 1;
            end >>= 1;
        }
        return res;
    }

    const numToIndex1 = {};
    for (let i = 0; i < N; i++) {
        numToIndex1[nums1[i]] = i;
    }
    const cntAfter = {};
    for (let i = N - 1; i > -1; i--) {
        const num = nums2[i];
        const index1 = numToIndex1[num];
        cntAfter[num] = query(index1, N, segTree);
        add(index1, segTree);
    }

    let res = 0;
    segTree.fill(0);
    for (let i = 0; i < N; i++) {
        const num = nums2[i];
        const index1 = numToIndex1[num];
        if (cntAfter[num]) {
            const cntBefore = query(0, index1 + 1, segTree);
            res += cntBefore * cntAfter[num];
        }
        add(index1, segTree);
    }
    return res;
};

