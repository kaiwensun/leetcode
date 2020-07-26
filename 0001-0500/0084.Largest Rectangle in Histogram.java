/**
 *Idea:
 * Dynamic programming. For a rect with height h, calculate and record its farthest expansion to left and right.
 * While calculating, make use of already calculated expansions.
 *Result:
 * 94 / 94 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 85.60% of javasubmissions.
 *Date:
 * 8/26/2016
 */
import java.util.Arrays;

public class Solution {
    private int[] lborder;
    private int[] rborder;
    private int[] heights;
    public int largestRectangleArea(int[] heights) {
        if(heights==null || heights.length==0)
            return 0;
        this.heights = heights;
        lborder = new int[heights.length];
        rborder = new int[heights.length];
        Arrays.fill(lborder, -1);
        Arrays.fill(rborder, -1);
        lborder[0] = 0;
        rborder[heights.length-1]=heights.length-1;
        for(int i=0;i<heights.length;i++){
        	getLBorder(i);
        }
        int max = 0;
        for(int i=heights.length-1;i>=0;i--){
        	getRBorder(i);
        	int area = (rborder[i]-lborder[i]+1)*heights[i]; 
        	max = area>max?area:max;
        }
        return max;
    }
    int getLBorder(int index){
    	int border = index;
    	while(border>0 && heights[border-1]>=heights[index])
    		border = lborder[border-1];
    	lborder[index] = border;
    	return border;
    }
    int getRBorder(int index){
    	int border = index;
    	while(border<heights.length-1 && heights[border+1]>=heights[index])
    		border = rborder[border+1];
    	rborder[index] = border;
    	return border;
    }
}
