int cmpint(const void* a, const void* b) {
    return *((int*)a) - *((int*)b);
}
int minOperations(int* nums, int numsSize){
    qsort(nums, numsSize, sizeof(int), cmpint);
    int unchanged = 0;
    int duplicates = 0;
    for (int i = 0, j = 0; i < numsSize; i++) {
        if (i != 0 && nums[i] == nums[i - 1]) {
            duplicates--;
            continue;
        }
        while (j < numsSize && nums[j] < nums[i] + numsSize) {
            if (j != 0 && nums[j] == nums[j - 1]) {
                duplicates++;
            }
            j++;
        }
        if (unchanged < j - i - duplicates) unchanged = j - i - duplicates;
    }
    return numsSize - unchanged;
}

