int sumOfBeauties(int* nums, int n){
    int* inc = (int*)malloc(sizeof(int) * n);
    int* dec = (int*)malloc(sizeof(int) * n);
    inc[0] = nums[0];
    dec[n - 1] = nums[n - 1];
    int res = 0;
    for (int i = 1; i < n; i++) {
        inc[i] = nums[i] > inc[i - 1] ? nums[i] : inc[i - 1];
        dec[n - 1 - i] = nums[n - 1 - i] < dec[n - i] ? nums[n - 1 - i] : dec[n - i];
    }
    for (int i = 1; i < n - 1; i++) {
        if (inc[i - 1] < nums[i] && nums[i] < dec[i + 1]) {
            res += 2;
        } else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
            res += 1;
        }
    }
    free(inc);
    free(dec);
    return res;
}

