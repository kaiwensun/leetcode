#include <stdlib.h>

int compare(const void* a, const void* b) { return *(int*)b - *(int*)a;}

long long minSumSquareDiff(int* nums1, int nums1Size, int* nums2, int nums2Size, int k1, int k2){
    int* diff = (int*) malloc(sizeof(int) * (nums1Size + 1));
    for (int i = 0; i < nums1Size; i++) {
        diff[i] = abs(nums1[i] - nums2[i]);
    }
    diff[nums1Size] = 0;
    qsort(diff, nums1Size, sizeof(*diff), compare);
    int k = k1 + k2;
    long i = 0, res = 0;
    while (diff[i] != 0) {
        int prev_i = i;
        while (diff[++i] == diff[prev_i]);
        if (i * (diff[prev_i] - diff[i]) <= k) {
            k -= i * (diff[prev_i] - diff[i]);
            if (k == 0 || diff[i] == 0) {
                res = i * diff[i] * diff[i];
                break;
            }
        } else {
            long long h1 = diff[prev_i] - k / i, h2 = h1 - 1;
            long long w2 = k % i, w1 = i - w2;
            res = h1 * h1 * w1 + h2 * h2 * w2;
            break;
        }
    }
    while (diff[i] > 0) {
        res += (long long)diff[i] * diff[i];
        i++;
    }
    free(diff);
    return res;
}

