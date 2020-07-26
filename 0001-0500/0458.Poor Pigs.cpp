/**
 *Basic idea:
 * Arrange buckets into a k-dimensional square matrix. the size of the matrix is n-by-n-by-n-by-n-...-by-n .
 * n is the number of (unposioned) buckets a pig can test in the given period.
 *Result:
 * 6 / 6 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 10.98% of cpp submissions.
 *Date:
 * 11/13/2016
 */
class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        return ceil(log(buckets)/log(minutesToTest/minutesToDie+1));
    }
};
