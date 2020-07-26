/**
 *Basic idea:
 * Topology sort. DFS. Add a special course called Graduation.
 *Result:
 * 36 / 36 test cases passed.
 * Status: Accepted
 * Runtime: 12 ms
 * Your runtime beats 62.62% of java submissions.
 *Date:
 * 10/2/2016
 */
public class Solution {
    class Course{
        int id;
        boolean taken = false;
        boolean visited = false;
        LinkedList<Integer> pre = new LinkedList<>();
        public Course(int id){
            this.id = id;
        }
    }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        ArrayList<Course> courses = new ArrayList<Course>(numCourses+1);
        for(int i=0;i<numCourses+1;i++){
            courses.add(new Course(i));
        }
        //set prerequisites
        for(int[] dep : prerequisites){
            courses.get(dep[0]).pre.add(dep[1]);
        }
        //assume the graduation needs all courses as prerequisites
        for(int i=0;i<numCourses;i++){
            courses.get(numCourses).pre.add(i);
        }
        ArrayList<Integer> schedule = new ArrayList<>(numCourses+1);
        if(dfs(schedule,courses,numCourses)){
            int[] res = new int[numCourses];
            for(int i=0;i<numCourses;i++){
                res[i] = schedule.get(i);
            }
            return res;
        }else{
            return new int[0];
        }
    }
    
    /**
     * @return the course can be completed
     */
    boolean dfs(ArrayList<Integer> schedule, ArrayList<Course> courses, int cid){
        if(courses.get(cid).taken){
            return true;
        }
        if(courses.get(cid).visited){
            return false;
        }
        courses.get(cid).visited = true;
        for(int preq : courses.get(cid).pre){
            if(dfs(schedule,courses,preq)==false){
                return false;
            }
        }
        schedule.add(cid);
        courses.get(cid).taken = true;
        return true;
    }
}
