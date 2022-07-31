function maximumsSplicedArray(nums1: number[], nums2: number[]): number {
    const sum1 = nums1.reduce((acc, num) => acc + num, 0);
    const sum2 = nums2.reduce((acc, num) => acc + num, 0);
    const diff = nums1.map((num1, i) => nums2[i] - num1);
    let res = 0, cur1 = sum1, cur2 = sum2;
    for (const num of diff) {
        cur1 += num; cur2 += num;
        cur1 = Math.max(sum1, cur1); cur2 = Math.min(-sum2, cur2);
        res = Math.max(res, cur1, -cur2);
    }
    return res;
};

