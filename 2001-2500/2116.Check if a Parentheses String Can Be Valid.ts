function canBeValid(s: string, locked: string): boolean {
    let min = 0, max = 0;
    for (let i = 0; i < locked.length; i++) {
        const changable = locked[i] === '0';
        if (changable) {
            max++;
            min--;
        } else {
            if (s[i] === '(') {
                min++;
                max++;
            } else {
                min--;
                max--;
            }
        }
        if (min < 0) {
            min += 2;
        }
        if (min > max || max < 0) {
            return false;
        }
    }
    return min === 0;
};

