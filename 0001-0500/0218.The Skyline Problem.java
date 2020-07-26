/**
 *Basic idea:
 * 1. Each building is viewed as a start point and an end point.
 * 2. Sort all points according to horizontal position.
 * 3. Scan all point hights from left to right. Add start, remove end. Use a priorityqueue to store currently largest values.
 *Result:
 * 33 / 33 test cases passed.
 * Status: Accepted
 * Runtime: 248 ms
 * Your runtime beats 53.50% of java submissions.
 *Date:
 * 12/12/2016
 */
class Point implements Comparable{
    int x;
    int y;
    boolean start;
    Point(int x, int y, boolean start){
        this.x = x;
        this.y = y;
        this.start = start;
    }
    @Override
    public int compareTo(Object other){
        Point a = this;
        Point b = (Point)other;
        if(a.x!=b.x){
            return a.x-b.x;
        }else{
            if(a.start && b.start){
                return b.y-a.y;
            }else if(!a.start && !b.start){
                return a.y-b.y;
            }else if(a.start){
                return -1;
            }else{
                return 1;
            }
        }
    }
}
public class Solution {
    
    public List<int[]> getSkyline(int[][] buildings) {
        List<Point> pts = sortPoints(buildings);
        PriorityQueue<Integer> pq = new PriorityQueue<>(buildings.length+1,new Comparator<Integer>(){
            @Override
            public int compare(Integer a, Integer b){
                return b-a;
            }
        });
        pq.offer(0);
        List<int[]> res = new LinkedList<>();
        int height = -1;
        for(Point pt : pts){
            if(pt.start){
                pq.offer(pt.y);
            }else{
                pq.remove(pt.y);
            }
            if(pq.peek()!=height){
                height = pq.peek();
                res.add(new int[]{pt.x,height});
            }
        }
        return res;
    }
    private List<Point> sortPoints(int[][] buildings){
        List<Point> pts = new ArrayList<>(buildings.length*2);
        for(int[] building : buildings){
            pts.add(new Point(building[0],building[2],true));
            pts.add(new Point(building[1],building[2],false));
        }
        Collections.sort(pts);
        return pts;
    }
}
