function countCollisions(directions: string): number {
    const arr = [];
    for (const dir of directions) {
        if (!arr.length && dir === 'L') continue;
        arr.push(dir);
    }
    while (arr.length && arr[arr.length - 1] === 'R') {
        arr.pop();
    }
    return arr.filter(item => item !== 'S').length;
};

