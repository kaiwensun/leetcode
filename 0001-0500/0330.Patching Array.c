int minPatches(int* nums, int numsSize, int n){
    int res = 0, i = 0;
    long x = 1;
    while (x <= n) {
        if (i < numsSize && nums[i] <= x) {
            x += nums[i++];
        } else {
            res++;
            x *= 2;
        }
    }
    return res;
}

