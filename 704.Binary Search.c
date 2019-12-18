int search(int* nums, int numsSize, int target){
    int *left = nums, *right = nums + numsSize;
    while (left < right) {
        int *mid = left + (right - left) / 2;
        printf("%d, %d, %d\n", left - nums, right - nums, mid - nums);
        if (*mid < target) left = mid + 1;
        else right = mid;
    }
    // printf("%d\n", *left);
    return left < nums + numsSize && *left == target ? left - nums : -1;
}
