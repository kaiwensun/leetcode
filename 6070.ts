function digitSum(s: string, k: number): string {
    while (s.length > k) {
        const res = [];
        for (let i = 0; i < s.length; i += k) {
            res.push([...s.substr(i, k)].map(d => parseInt(d)).reduce((acc, num) => acc + num, 0));
        }
        s = res.join("");
    }
    return s;
};


