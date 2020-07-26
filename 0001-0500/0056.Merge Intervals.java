/**
 *Result:
 * 168 / 168 test cases passed.
 * Status: Accepted
 * Runtime: 27 ms
 * Your runtime beats 62.84% of java submissions.
 *Date:
 * 10/27/2016
 */
 
/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    private final static Comparator<Interval> comparator = new Comparator<Interval>(){
          @Override
          public int compare(Interval a, Interval b){
              if(a.start<b.start || (a.start==b.start && a.end>b.end)){
                  return -1;
              }else if(a.start==b.start && a.end==b.end){
                  return 0;
              }else{
                  return 1;
              }
          }
        };
    public List<Interval> merge(List<Interval> intervals) {
        Collections.sort(intervals,comparator);
        List<Interval> res = new LinkedList<Interval>();
        Interval cur = null;
        
        for(Interval itvl : intervals){
            if(cur==null){
                cur = itvl;
            }else if(itvl.start==cur.start){
                continue;
            }else{
                if(cur.end<itvl.start){
                    res.add(cur);
                    cur = itvl;
                }else{
                    cur.end = Math.max(cur.end,itvl.end);
                }
            }
        }
        if(cur!=null){
            res.add(cur);
        }
        return res;
    }
}
