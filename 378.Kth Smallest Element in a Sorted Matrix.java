/**
 *Result:
 * 85 / 85 test cases passed.
 * Status: Accepted
 * Runtime: 36 ms
 * Your runtime beats 35.63% of java submissions.
 *Date:
 * 10/16/2016
 */
public class Solution {
    class Node{
        int i;
        int j;
        int val;
        public Node(int val,int i,int j){
            this.i = i;
            this.j = j;
            this.val = val;
        }
    }
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<Node> heap = new PriorityQueue<>(n*2-1, new Comparator<Node>(){
                @Override
                public int compare(Node a, Node b){
                    return a.val-b.val;
                }
            });
        for(int i=0;i<n;i++){
            heap.offer(new Node(matrix[i][0],i,0));
        }
        for(int j=1;j<n;j++){
            heap.offer(new Node(matrix[0][j],0,j));
        }
        Node node = null;
        while(k>0){
            node = heap.poll();
            int i = node.i;
            int j = node.j;
            if(i+1<n && j+1<n){
                heap.offer(new Node(matrix[i+1][j+1],i+1,j+1));
            }
            k--;
        }
        return node.val;
    }
}
