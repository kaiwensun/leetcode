bool xorGame(int* nums, int numsSize){
    if (numsSize & 1) {
        int xor = 0;
        for (int i = 0; i < numsSize; i++) {
            xor ^= nums[i];
        }
        return xor == 0;
    }
    return true;
}

