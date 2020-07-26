/**
 *Result:
 * 14 / 14 test cases passed.
 * Status: Accepted
 * Runtime: 976 ms
 *Date:
 * 10/20/2016
 */
SELECT Emp.Name AS 'Employee'
FROM Employee Emp, Employee Mgr
WHERE Emp.ManagerId = Mgr.Id
    AND Emp.Salary>Mgr.Salary;

