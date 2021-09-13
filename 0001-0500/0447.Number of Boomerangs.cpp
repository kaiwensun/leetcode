/**
 *Result:
 * 31 / 31 test cases passed.
 * Status: Accepted
 * Runtime: 1219 ms
 * Your runtime beats 100.00% of cpp submissions.
 */
class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
		int res = 0;
		for (int i = 0; i < points.size(); i++){
			unordered_map<int, int> hashMap;	//<key,value> = <sqrd_distance, count>
			for (int j = 0; j < points.size(); j++){
				if (j == i){
					continue;
				}
				int dist = getDist(points[i], points[j]);
				hashMap[dist]++;
			}
			for (auto d : hashMap){
				res += cntChooseTwo(d.second);
			}
		}
		return res;
	}
private:
	int getDist(vector<int> point1, vector<int> point2){
		return (point1[0] - point2[0])*(point1[0] - point2[0])
			+ (point1[1] - point2[1])*(point1[1] - point2[1]);
	}
	
	inline int cntChooseTwo(int n){
		return (n*(n - 1));
	}
};

