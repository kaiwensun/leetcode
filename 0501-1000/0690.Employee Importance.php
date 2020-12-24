/**
 * Definition for Employee.
 * class Employee {
 *     public $id = null;
 *     public $importance = null;
 *     public $subordinates = array();
 *     function __construct($id, $importance, $subordinates) {
 *         $this->id = $id;
 *         $this->importance = $importance;
 *         $this->subordinates = $subordinates;
 *     }
 * }
 */

class Solution {
    function dfs($id) {
        return $this->graph[$id]->importance + array_sum(array_map(array($this, 'dfs'), $this->graph[$id]->subordinates));
    }

    /**
     * @param Employee[] $employees
     * @param Integer $id
     * @return Integer
     */
    function getImportance($employees, $id) {
        $this->graph = array();
        foreach($employees as $employee) {
            $this->graph[$employee->id] = $employee;
        }
        return $this->dfs($id);
    }

}

