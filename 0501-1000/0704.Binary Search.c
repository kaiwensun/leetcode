int search(int* nums, int numsSize, int target){
    int *left = nums, *right = nums + numsSize;
    while (left < right) {
        int *mid = left + (right - left) / 2;
        if (*mid < target) left = mid + 1;
        else right = mid;
    }
    return left < nums + numsSize && *left == target ? left - nums : -1;
}
