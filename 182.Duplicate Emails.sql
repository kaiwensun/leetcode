/*
 *Result:
 * 14 / 14 test cases passed.
 * Status: Accepted
 * Runtime: 598 ms
 * Your runtime beats 95.43% of mysql submissions.
 *Date:
 * 10/20/2016
 */
SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*)>1;
