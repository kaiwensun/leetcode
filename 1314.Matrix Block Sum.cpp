class Solution {
public:
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                if (j != 0) mat[i][j] += mat[i][j - 1];
                if (i != 0) mat[i][j] += mat[i - 1][j];
                if (i != 0 && j != 0) mat[i][j] -= mat[i - 1][j - 1];
            }
        }
        vector<vector<int>> answer;
        answer.resize(mat.size());
        int H = mat.size() - 1;
        int W = mat[0].size() - 1;
        for (int i = 0; i < answer.size(); i++) {
            answer[i].resize(mat[i].size());
            for (int j = 0; j < answer[i].size(); j++) {
                answer[i][j] = mat[min(i + K, H)][min(W, j + K)]
                    - (j > K ? mat[min(H, i + K)][j - K - 1] : 0)
                    - (i > K ? mat[i - K - 1][min(W, j + K)] : 0)
                    + (i > K && j > K ? mat[i - K - 1][j - K - 1] : 0);
            }
        }
        return answer;
    }
};
