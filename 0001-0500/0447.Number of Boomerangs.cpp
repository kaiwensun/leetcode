/**
 *Result:
 * 31 / 31 test cases passed.
 * Status: Accepted
 * Runtime: 1219 ms
 * Your runtime beats 100.00% of cpp submissions.
 */
class Solution {
public:
	int numberOfBoomerangs(vector<pair<int, int>>& points) {
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
	int getDist(pair<int, int> point1, pair<int, int> point2){
		return (point1.first - point2.first)*(point1.first - point2.first)
			+ (point1.second - point2.second)*(point1.second - point2.second);
	}
	
	inline int cntChooseTwo(int n){
		return (n*(n - 1));
	}
};
