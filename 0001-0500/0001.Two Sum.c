/*
(Any idea to have secure O(n) C code regardless of the border of testcases?)

[1] 4ms O(n) time, very large constant space, insecure C code (insecure when large constant is not large enough).

Idea: hash value to index. I.e. use value as new index of a hash_table to store original index.
Oh, if we allow collision of hashtable, use hashtable[(nums[i] + ABSMAX)%MAX] instead of hash_table[nums[i] + ABSMAX], and do some minor collision checks, then the O(n) algorithm can be secure.
*/
#include<stdlib.h>
#include<string.h>
/**
* Note: The returned array must be malloced, assume caller calls free().
*/
#define MAX 50000
#define ABSMAX MAX/2
int* map(int nums[],int numsSize,int target,int* answer1,int* answer2)
{
    int *hash_table = (int*)malloc(sizeof(int)*MAX);
    memset(hash_table, 0, sizeof(int)*MAX);
    for (int i = 0; i < numsSize; i++)
    {
        if (hash_table[nums[i] + ABSMAX] != 0)    //INSECURE if (nums[i]+ABSMAX) exceeds border
        {
            if (target == nums[i] * 2)  //if x+x=target, avoid hash-collision
            {
                *answer1 = hash_table[nums[i] + ABSMAX];
                *answer2 = i + 1;
                return NULL;
            }
        }
        hash_table[nums[i] + ABSMAX] = i + 1;   //map value to index, INSECURE
    }
    return hash_table;
}
int* twoSum(int nums[], int numsSize, int target) {
    int answer1, answer2;
    int* hash_table = map(nums, numsSize,target,&answer1,&answer2); //create hash_table, time: O(n)
    if (hash_table != NULL)     //check hash_table, time:O(n)
    {
        for (int i = 0; i < numsSize; i++)
        {
            int number = nums[i];
            int partner = target - number;
            if (hash_table[partner + ABSMAX] != 0)
            {
                answer1 = i+1;
                answer2 = hash_table[partner + ABSMAX];
                if (answer1 == answer2)
                    continue;
                break;
            }
        }
    }
    //make answer
    if (answer1 > answer2)
    {
        int tmp = answer1; answer1 = answer2; answer2 = answer1;
    }
    int* rtn = (int*)malloc(sizeof(int)* 2);
    rtn[0] = answer1;
    rtn[1] = answer2;
    return rtn; 
}
/*
[2] 4ms O(n logn) time, O(n) space, secure C code

Idea: qsort (but track original index), then for every element x in the array find() whether target-x exists. Since the array is sorted, every find() costs logn time.
*/
#include<stdio.h>
#include<stdlib.h>
/**
* Note: The returned array must be malloced, assume caller calls free().
*/
struct Locator
{
    int number;
    int index;
}* locator;
int compare(struct Locator* a, struct Locator* b)
{
    return a->number - b->number;
}
int findPartnerIndex(struct Locator nums[], int left, int right, int partner)
{
    if (left == right)
    {
        if (nums[left].number == partner)
            return left;
        return -1;
    }
    if (nums[left].number>partner || nums[right].number<partner)
        return -1;
    int mid = (left + right) / 2;
    if (nums[mid].number == partner)
        return mid;
    if (nums[mid].number < partner)
        return findPartnerIndex(nums, mid + 1, right, partner);
    else
        return findPartnerIndex(nums, left, mid - 1, partner);
}
int* twoSum(int nums[], int numsSize, int target) {
    int a = 0, b = 0;
    locator = (struct Locator*)malloc(sizeof(struct Locator)*numsSize);
    for (int i = 0; i < numsSize; i++)
    {
        locator[i].number = nums[i];
        locator[i].index = i;
    }
    qsort(locator, numsSize, sizeof(struct Locator), compare);
    for (int i = 0; i < numsSize; i++)
    {
        //printf("%d\n", i);
        int partnerIndex = findPartnerIndex(locator, 0, numsSize - 1, target - locator[i].number);
        if (partnerIndex == -1)
            continue;
        if (i == partnerIndex)
        {
            if (locator[i].number == locator[i + 1].number)
            {
                a = i; b = i + 1;
                break;
            }
            continue;
        }
        a = i; b = partnerIndex;
        break;
    }
    int* rtn = malloc(sizeof(int)* 2);
    rtn[0] = locator[a].index+1;
    rtn[1] = locator[b].index+1;
    if (rtn[1] < rtn[0])
    {
        int tmp = rtn[0]; rtn[0] = rtn[1]; rtn[1] = tmp;
    }
    return rtn;
}

