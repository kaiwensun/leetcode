/**
 *Result:
 * 12 / 12 test cases passed.
 * Status: Accepted
 * Runtime: 461 ms
 * Your runtime beats 87.03% of mysql submissions.
 *Date:
 * 10/20/2016
 */
SELECT Name AS 'Customers'
FROM Customers
WHERE Id not in (
    SELECT CustomerId
    FROM Orders
);
