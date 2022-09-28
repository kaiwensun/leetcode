int stack[10001] = {-1};

int validSubarraySize(int* nums, int numsSize, int threshold){
    int* sp = stack;
    for (int i = 0; i <= numsSize; i++) {
        while (sp != stack && (i == numsSize || nums[*sp] >= nums[i])) {
            int k = i - *(sp - 1) - 1;
            int mn = nums[*sp];
            if (nums[*sp] * k > threshold) {
                return k;
            }
            sp--;
        }
        *++sp = i;
    }
    return -1;
}

