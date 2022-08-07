function maximumGroups(grades: number[]): number {
    grades.sort((a, b) => a - b);
    let res = 0, preve_grade_sum = 0, prev_cnt_sum = 0, grade_sum = 0, cnt_sum = 0;
    for (const grade of grades) {
        grade_sum += grade;
        cnt_sum++;
        if (grade_sum > preve_grade_sum && cnt_sum > prev_cnt_sum) {
            preve_grade_sum = grade_sum;
            grade_sum = 0;
            prev_cnt_sum = cnt_sum;
            cnt_sum = 0;
            res++;
        }
    }
    return res;
};

