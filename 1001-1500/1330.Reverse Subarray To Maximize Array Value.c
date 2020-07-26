int max(int a, int b) { return a > b ? a : b;}
int min(int a, int b) { return a < b ? a : b;}
int abs(int a) {return max(a, -a);}
int currentValue(int* nums, int numsSize) {
    int res = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        res += abs(nums[i] - nums[i + 1]);
    }
    return res;
}
int maxValueAfterReverse(int* nums, int numsSize){
    int mn = 100000, mx = -100000, inc = 0;
    for (int i = 0; i < numsSize - 1; i++) {
        mn = min(mn, max(nums[i], nums[i + 1]));
        mx = max(mx, min(nums[i], nums[i + 1]));
    }
    inc = max(inc, (mx - mn) * 2);
    for (int i = 0; i < numsSize - 1; i++) {
        inc = max(inc, abs(nums[0] - nums[i + 1]) - abs(nums[i] - nums[i + 1]));
        inc = max(inc, abs(nums[numsSize - 1] - nums[i]) - abs(nums[i] - nums[i + 1]));
    }
    return currentValue(nums, numsSize) + inc;
}
