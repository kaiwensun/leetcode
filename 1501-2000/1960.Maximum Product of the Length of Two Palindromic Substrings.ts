/*
 Get familiar with Manacher's algorithm first by looking at 0005.Longest Palindromic Substring.ts 
*/
function maxProduct(s: string): number {
    const p: number[] = [];
    const sizesOfEnd: number[] = new Array(s.length);
    const sizesOfStart: number[] = new Array(s.length);
    const maxSizes: number[] = new Array(s.length);
    let k = 0;
    let maxRight = -1, center = -1;
    for (let i = 0; i < s.length; i++) {
        let l: number, r: number;
        if (i > maxRight) {
            r = i + 1;
            l = i - 1;
        } else {
            const j = center + center - i;
            const expand = Math.min(Math.ceil(p[j] / 2), maxRight - i + 1);
            r = i + expand;
            l = i - expand;
        }
        while (l >= 0 && r < s.length && s[l] === s[r]) {
            l--; r++;
        }
        p.push(r - l - 1);
        if (r - 1 > maxRight) {
            maxRight = r - 1;
            center = i;
        }
        while (k <= maxRight) {
            sizesOfEnd[k] = (k - center) * 2 + 1;
            maxSizes[k] = Math.max(maxSizes[k - 1] || 0, sizesOfEnd[k]);
            k++;
        }
    }
    let leftMost = s.length - 1;
    center = s.length - 1;
    k = s.length - 1;
    for (let i = s.length - 1; i >= 0; i--) {
        if (i - Math.floor(p[i] / 2) < leftMost) {
            leftMost = i - Math.floor(p[i] / 2);
            center = i;
        }
        while (k >= leftMost) {
            sizesOfStart[k] = (center - k) * 2 + 1;
            k--;
        }
    }
    let res = 0;
    for (let start2 = s.length - 1; start2 > 0; start2--) {
        let size2 = sizesOfStart[start2];
        let size1 = maxSizes[start2 - 1];
        res = Math.max(res, size1 * size2);
    }
    return res;
};

