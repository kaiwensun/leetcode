/**
 *Basic idea:
 * use the first row and column to mark whether the row or column should be set to zeros.
 *Result:
 * 157 / 157 test cases passed.
 * Status: Accepted
 * Runtime: 56 ms
 * Your runtime beats 76.82% of cpp submissions.
 *Date:
 * 10/2/2016
 */
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        //special case check
        if(matrix.size()==0 || matrix[0].size()==0){
            return;
        }
        //check first row & col
        bool fstRowHas0 = false;
        bool fstColHas0 = false;
        for(vector<int>::iterator it = matrix[0].begin();it!=matrix[0].end();it++){
            if(*it==0){
                fstRowHas0 = true;
                break;
            }
        }
        for(vector<vector<int>>::iterator it = matrix.begin();it!=matrix.end();it++){
            if(*(*it).begin()==0){
                fstColHas0 = true;
                break;
            }
        }
        //mark rows & cols by setting 0s in first row & col
        for(int i=0;i<matrix.size();i++){
            for(int j=0;j<matrix[0].size();j++){
                if(matrix[i][j] == 0){
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        //fill rows and cols
        for(int i = 1;i<matrix.size();i++){
            if(matrix[i][0]==0){
                for(int j=0;j<matrix[0].size();j++){
                    matrix[i][j]=0;
                }
            }
        }
        for(int j = 1;j<matrix[0].size();j++){
            if(matrix[0][j]==0){
                for(int i=0;i<matrix.size();i++){
                    matrix[i][j]=0;
                }
            }
        }
        
        //fill first col and row
        if(fstRowHas0){
            for(int j=0;j<matrix[0].size();j++){
                matrix[0][j]=0;
            }
        }
        if(fstColHas0){
            for(int i=0;i<matrix.size();i++){
                matrix[i][0]=0;
            }
        }
    }
};
