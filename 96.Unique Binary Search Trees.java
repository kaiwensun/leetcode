/*	Basic idea:
 *		Dynamic programming
 *		[0]=1
 *		[1]=1
 *		[2]=[0]*[1]+[1]*[0]=1+1=(1)*2=2
 *		[3]=[0]*[2]+[1]*[1]+[2]*[0]=2+1+2=2*2+1=5
 *		[4]=([0]*[3]+[1]*[2])*2+0=....
 *	......
 *	Result:
 *		19 / 19 test cases passed.
 *		Status: Accepted
 *		Runtime: 0 ms
*/


public class Solution {
    public int numTrees(int n) {
        if(n<=1)
            return 1;
        int[] ways = new int[n+1];
        ways[0] = 1;
        ways[1] = 1;
        for(int i=2;i<=n;i++)
        {
            int halfsum = 0;
            for(int j=0;j<i/2;j++)
                halfsum+=ways[j]*ways[i-j-1];
            halfsum*=2;
            if(i%2==1)
                halfsum+=ways[i/2]*ways[i/2];
            ways[i]=halfsum;
        }
        return ways[n];
    }
}

