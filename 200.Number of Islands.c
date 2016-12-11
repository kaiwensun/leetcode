/**
 *Result:
 * 47 / 47 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 3.45% of c submissions.
 *Date:
 * 12/10/2016
 */
int d[] = {-1,0,1,0,-1};
int numIslands(char** grid, int gridRowSize, int gridColSize) {
    int cnt = 0;
    for(int r = 0;r<gridRowSize;r++){
        for(int c = 0;c<gridColSize;c++){
            cnt+= fillLand(grid,gridRowSize, gridColSize,r,c);
        }
    }
    return cnt;
}
int fillLand(char** grid, int gridRowSize, int gridColSize, int r, int c){

    if(r<0 || c < 0 || r >= gridRowSize || c >= gridColSize || *(*(grid+r)+c)!='1'){
        return 0;
    }
    *(*(grid+r)+c) = '2';
    for(int i=0;i<4;i++){
        fillLand(grid,gridRowSize, gridColSize, r+d[i],c+d[i+1]);
    }
    return 1;
}
