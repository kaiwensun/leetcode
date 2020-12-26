class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        int stu0 = std::count(students.begin(), students.end(), 0);
        int stu1 = students.size() - stu0;
        int stus[2] = {stu0, stu1};
        for (auto sand = sandwiches.begin(); sand != sandwiches.end() && stus[*sand] != 0; sand++) {
            stus[*sand]--;
        }
        return stus[0] | stus[1];
    }
};

