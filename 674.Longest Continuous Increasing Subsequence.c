#define max(x,y) ((x) > (y) ? (x) : (y))
#define MAX_INT 1 << (sizeof(int) * 8 - 1) - 1

int findLengthOfLCIS(int* nums, int numsSize){
    int curNum = MAX_INT, res = 0, curSeqLen = 0;
    for (int i = 0; i < numsSize; i++) {
        curNum < nums[i] ? curSeqLen++ : (curSeqLen = 1);
        res = max(res, curSeqLen);
        curNum = nums[i];
    }
    return res;
}
