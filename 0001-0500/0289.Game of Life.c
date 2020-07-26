/**
 *Result:
 * 22 / 22 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 0.00% of c submissions
 *Date:
 * 9/23/2016
 */
const int maskNext = 2;
const int maskCurr = 1;
#define min(x,y) (x<y?x:y)
#define max(x,y) (x>y?x:y)
void decideLive(int** board,int r,int c,int boardRowSize, int boardColSize){
    int cnt = 0;
    for(int i=max(r-1,0);i<min(r+2,boardRowSize);i++){
        for(int j=max(c-1,0);j<min(c+2,boardColSize);j++){
            if(i==r && j==c)
                continue;
            if(board[i][j] & maskCurr == 1)
                cnt++;
        }
    }
    if(board[r][c]==0){
        if(cnt==3)
            board[r][c]=2;
    }
    else{
        if(cnt==2 || cnt==3){
            board[r][c]|=2;
        }
    }
}
void gameOfLife(int** board, int boardRowSize, int boardColSize) {
    for(int r=0;r<boardRowSize;r++){
        for(int c=0;c<boardColSize;c++){
            decideLive(board,r,c,boardRowSize,boardColSize);
        }
    }
    for(int r=0;r<boardRowSize;r++){
        for(int c=0;c<boardColSize;c++){
            board[r][c]=board[r][c]>>1;
        }
    }
}
