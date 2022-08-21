function shiftingLetters(s: string, shifts: number[][]): string {
    function doShift(c: string, shift: number) {
        return String.fromCharCode(97 + ((c.charCodeAt(0) - 97 + shift) % 26 + 26) % 26);
    }
    // [point, plus(true)/minus(false)]
    const points: number[][] = [];
    for (const [start, end, direction] of shifts) {
        points.push([start, direction ? 1 : -1]);
        points.push([end + 1, direction ? -1 : 1]);
    }
    points.sort((a, b) => b[0] - a[0]);
    const arr = [...s];
    let shift = 0, j = 0;
    for (let i = 0; i < s.length; i++) {
        while (points.length && points[points.length - 1][0] == i) {
            shift += points.pop()[1];
        }
        arr[i] = doShift(arr[i], shift);
    }
    return arr.join("");
};

