class Solution {
private:
    static const int MOD = 1000000007;
public:
    int countOrders(int n) {
        static vector<int> dp{1};
        if (n <= dp.size()) {
            return dp[n - 1];
        }
        dp.push_back((long long int)(2 * n - 1) * n * countOrders(n - 1) % MOD);
        return dp[dp.size() - 1];
    }
};
