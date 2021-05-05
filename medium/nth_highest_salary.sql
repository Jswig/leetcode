/* Anders Poirel
 *
 * https://leetcode.com/problems/nth-highest-salary
 *
 * Runtime: 304 ms, faster than 60.75% of MySQL online submissions for Nth Highest Salary.
 * Memory Usage: 0B, less than 100.00% of MySQL online submissions for Nth Highest Salary. */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N-1;
  RETURN (
      SELECT DISTINCT Salary 
      FROM Employee
      ORDER BY Salary DESC
      LIMIT 1 OFFSET M
      
  );
END