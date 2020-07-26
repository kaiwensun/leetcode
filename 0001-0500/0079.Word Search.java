/**
 * Basic idea:
 * 	brute force search and backtracking.
 * Result:
 * 	87 / 87 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 12 ms
 * 	Your runtime beats 72.09% of java submissions.
 * Date:
 * 	2/7/2016
 * Comment:
 * 	At first, I passed newly created substring to makeOneStep(). It is very inefficient to creat new object frequently. Now a revised version passes the reference to the original word and a start index to makeOneStep(). Before that, the program beated only 19.21% of submissions and took 21ms. After that, it beats 72.09% and takes 12 ms.
 */
public class Solution {
    private char[][] board;
    public boolean exist(char[][] board, String word) {
        if(board==null || board.length==0 || board[0]==null || board[0].length==0)
            return false;
        this.board = board;
        for(int row = 0;row<board.length;row++)
            for(int col = 0;col<board[0].length;col++)
                if(makeOneStep(row,col,word,0))
                    return true;
        return false;
    }
    private boolean makeOneStep(int row, int col,String word,int start){
        if(word.length()==start)
            return true;
        if(row<0 ||row>=board.length||col<0||col>=board[0].length)
            return false;
        if(board[row][col]!=word.charAt(start))
            return false;
        char thischar = board[row][col];
        board[row][col]='-';
        boolean result = makeOneStep(row, col-1,word,start+1)
                || makeOneStep(row-1, col,word,start+1)
                || makeOneStep(row, col+1,word,start+1)
                || makeOneStep(row+1, col,word,start+1);
        board[row][col]=thischar;
        return result;
    }
}

