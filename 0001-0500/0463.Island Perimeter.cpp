class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int sideCnt = 0;
        if(grid.size()!=0 && grid[0].size()!=0){
            for(int i=0;i<grid.size();i++){
                sideCnt += grid[i][0];
                for(int j=0;j<grid[0].size()-1;j++){
                    sideCnt += grid[i][j]^grid[i][j+1];
                }
                sideCnt += grid[i][grid[i].size()-1];
            }
            for(int i=0;i<grid.size()-1;i++){
                for(int j=0;j<grid[0].size();j++){
                    sideCnt += grid[i][j]^grid[i+1][j];
                }
            }
            for(int j=0;j<grid[0].size();j++){
                sideCnt+=grid[0][j]+grid[grid.size()-1][j];
            }
        }
        return sideCnt;
    }
};
