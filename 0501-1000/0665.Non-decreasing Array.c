bool checkPossibility(int* nums, int numsSize){
    bool modified = false;
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] < nums[i - 1]) {
            if (modified) {
                return false;
            }
            if (i != 1 && !(i >= 2 && nums[i - 2] <= nums[i])) {
                nums[i] = nums[i - 1];
            }
            modified = true;
        }
    }
    return true;
}

