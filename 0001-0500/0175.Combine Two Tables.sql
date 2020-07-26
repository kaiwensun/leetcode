/*
 *Result:
 * 7 / 7 test cases passed.
 * Status: Accepted
 * Runtime: 738 ms
 * Your runtime beats 6.13% of mysql submissions.
 *Date:
 * 10/20/2016
 */

SELECT
    FirstName,
    LastName,
    City,
    State
FROM
    Person
LEFT JOIN Address ON
    Person.PersonID=Address.PersonID;
