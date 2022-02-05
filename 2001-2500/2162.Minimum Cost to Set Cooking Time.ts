function minCostSetTime(startAt: number, moveCost: number, pushCost: number, targetSeconds: number): number {
    function toChars([minutes, seconds]: number[]) {
        if (minutes) {
            const chars = ('' + minutes).split('');
            return chars.concat(String(seconds).padStart(2, '0').split(''));
        } else {
            return ('' + seconds).split('');
        }
    }

    function cost([minutes, seconds]: number[]) {
        if (minutes < 0 || minutes > 99 || seconds < 0 || seconds > 99) {
            return Infinity;
        }
        const chars = toChars([minutes, seconds]);
        let res = 0;
        let prevChar = '' + startAt;
        for (const char of chars) {
            if (char !== prevChar) {
                prevChar = char;
                res += moveCost;
            }
            res += pushCost;
        }
        return res;
    }

    function standardTime() {
        const seconds = targetSeconds % 60;
        const minutes = (targetSeconds - seconds) / 60;
        return [minutes, seconds];
    }

    function extraSecondsTime() {
        let [minutes, seconds] = standardTime();
        return [minutes - 1, seconds + 60];
    }

    return Math.min(
        cost(standardTime()),
        cost(extraSecondsTime())
    )
};

