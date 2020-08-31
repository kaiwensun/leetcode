/**
 *Result:
 * 14 / 14 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 41.55% of java submissions.
 *Date:
 * 11/7/2016
 */
public class Solution {
    
    private static final char[] DNAs = new char[]{'A','C','G','T'};
    public int minMutation(String start, String end, String[] bank) {
        //corner case
        if(start==null || end==null || start.length()!=end.length()){
            return -1;
        }
        if(bank==null || bank.length==0){
            if(start.equals(end)){
                return 0;
            }else{
                return -1;
            }
        }
        
        Set<String>bankSet = new HashSet<>(bank.length);
        for(String str:bank){
        	bankSet.add(str);
        }
        //init BFS queue
        Deque<String>queue = new LinkedList<>();
        queue.offer(start);
        queue.offer("#");
        
        boolean changed = true;
        int step = 0;
        while((changed || queue.peekLast().equals("#"))&& queue.size()>1){
        	String curr = queue.poll();
        	if(curr.equals("#")){
        		step++;
        		changed = false;
        		queue.offer("#");
        	}else if(curr.equals(end)){
        		return step;
        	}else{
        		boolean hasNext = false;
        		StringBuilder sb = new StringBuilder(curr);
        		for(int i=0;i<sb.length();i++){
        			char buff = sb.charAt(i);
        			for(char c:DNAs){
        				if(buff==c){
        					continue;
        				}
        				sb.setCharAt(i, c);
        				String nxt = sb.toString();
        				if(bankSet.contains(nxt)){
        					if(nxt.equals(end)){
        						return step+1;
        					}
        					hasNext = true;
        					changed = true;
        					bankSet.remove(nxt);
        					queue.offer(nxt);
        				}
        			}
        			sb.setCharAt(i,buff);
        		}
        		if(!hasNext){
        			queue.offer(curr);
        		}
        	}
        	
        }
        return -1;
    }
}
