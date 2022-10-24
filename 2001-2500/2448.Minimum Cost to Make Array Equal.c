long long totalCost( int avg, int* nums, int* cost, int size) {
    long long res = 0;
    for (int i = 0; i < size; i++) {
        res += abs(nums[i] - avg) * (long long)cost[i];
    }
    return res;
}

long long minCost(int* nums, int numsSize, int* cost, int costSize) {
    const int MN = 0, MX = 1000000;
    int left = MN, right = MX;
    while (left < right) {
        int mid = (left + right) / 2;
        long long mres = totalCost(mid, nums, cost, numsSize);
        if (mres > totalCost(mid - 1, nums, cost, numsSize)) right = mid - 1;
        else if (mres > totalCost(mid + 1, nums, cost, numsSize)) left = mid + 1;
        else left = right = mid;
    }
    return totalCost(left, nums, cost, numsSize);
}

