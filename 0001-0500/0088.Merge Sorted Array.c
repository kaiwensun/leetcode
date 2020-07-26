/*
Basic idea:
	For oridinary mergesort, we merge from the heading. However, in this problem the heading array is temporarily used.
	Since the array is increasingly sorted from head to tail, it is equivalent to an array decreasingly sorted from tail to head. We can merge from tail to head, and plcae the result from tail to head.

59 / 59 test cases passed.
Status: Accepted
Runtime: 0 ms
Your runtime beats 10.49% of c submissions.
*/
void merge(int* nums1, int m, int* nums2, int n) {
    int target = m+n-1;
    m--;n--;
    while(m>=0 && n>=0)
        if (nums1[m]>nums2[n])
            nums1[target--]=nums1[m--];
        else
            nums1[target--]=nums2[n--];
    if (n>=0)
        memcpy(nums1, nums2, sizeof(int)*(n+1));
}

