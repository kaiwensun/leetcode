function addSpaces(s: string, spaces: number[]): string {
    spaces.push(s.length);
    let i = 0;
    const res = [];
    for (let j of spaces) {
        res.push(s.substring(i, j));
        i = j;
    }
    return res.join(" ");
};

