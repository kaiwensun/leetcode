function checkRecord(s: string): boolean {
    let absent = 0, late = 0;
    for (let c of s) {
        if (c === 'A') {
            absent++;
            late = 0;
        } else if (c === 'L') {
            late++;
        } else {
            late = 0;
        }
        if (absent == 2 || late == 3) {
            return false;
        }
    }
    return true;
};

