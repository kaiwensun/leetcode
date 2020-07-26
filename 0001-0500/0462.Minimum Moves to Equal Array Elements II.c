#include <stdlib.h>

#define abs(a) (a < 0) ? (-(a)) : (a)

int getRankOfFirst(int* first, int* last) {
    int pivot = *first;
    int *l = first, *r = last;
    int* p = first + 1;
    while (l < r) {
        if (*p <= pivot) {
            *l++ = *p++;
        } else {
            int tmp = *r;
            *r-- = *p;
            *p = tmp;
        }
    }
    *l = pivot;
    return l - first;
}

int findNth(int* first, int* last, int index) {
    int rank = getRankOfFirst(first, last);
    if (rank == index) {
        return first[index];
    } else if (rank < index) {
        return findNth(first + rank + 1, last, index - rank - 1);
    } else {
        return findNth(first, first + rank - 1, index);
    }
}

int findMedian(int* nums, int numsSize) {
    return findNth(nums, nums + numsSize - 1, (numsSize - 1) / 2);
}

int minMoves2(int* nums, int numsSize){
    int median = findMedian(nums, numsSize);
    int res = 0;
    int i;
    for (i = 0; i < numsSize; i++) {
        res += abs(median - nums[i]);
    }
    return res;
}
