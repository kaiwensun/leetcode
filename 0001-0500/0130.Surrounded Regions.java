/**
 *Result:
 * 58 / 58 test cases passed.
 * Status: Accepted
 * Runtime: 20 ms
 * Your runtime beats 12.71% of java submissions.
 *Date:
 * 9/30/2016
 */
public class Solution {
    public void solve(char[][] board) {
        if(board==null || board.length==0)
            return;
        int db = 0;
        for(int c = 0;c<board[0].length;c++){
            fillArea(board,'O','#',0,c);
            fillArea(board,'O','#',board.length-1,c);
        }
        for(int r=0;r<board.length;r++){
            fillArea(board,'O','#',r,0);
            fillArea(board,'O','#',r,board[0].length-1);
        }
        for(int r=0;r<board.length;r++){
            for(int c=0;c<board[0].length;c++){
                if(board[r][c]=='O')
                    board[r][c]='X';
                if(board[r][c]=='#')
                    board[r][c]='O';
            }
        }
    }
    private void fillArea(char[][] board, char from, char to, int x, int y){
        if(!isValidCell(board,x,y)){
            return;
        }
        if(board[x][y]==from){
            board[x][y] = to;
            Stack<Integer> X = new Stack<>();
            Stack<Integer> Y = new Stack<>();
            X.push(x);
            Y.push(y);
            
            int[] xarr = {-1,+1,0,0};
            int[] yarr = {0,0,-1,+1};
            while(!X.isEmpty()){
                x = X.pop();
                y = Y.pop();
                for(int i=0;i<4;i++){
                    int r=x+xarr[i];
                    int c=y+yarr[i];
                    if(isValidCell(board,r,c) && board[r][c]==from){
                        board[r][c] = to;
                        X.push(r);
                        Y.push(c);
                    }
                }
            }
        }
    }
    
    private boolean isValidCell(char[][] board, int x, int y){
        return !(x<0 || x>=board.length || y<0 || y>=board[0].length);
    }
}
