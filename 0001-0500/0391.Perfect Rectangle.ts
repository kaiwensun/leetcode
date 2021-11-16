function isRectangleCover(rectangles: number[][]): boolean {
    const set = new Set();
    rectangles.forEach(([x, y, a, b]) => {
        [[x, y], [x, b], [a, y], [a, b]].forEach(point => {
            const pStr = point.toString();
            if (set.has(pStr)) {
                set.delete(pStr);
            } else {
                set.add(pStr);
            }
        })
    });
    if (set.size != 4) {
        return false;
    }
    const corners = [0, 1, 2, 3].map(i => (i < 2 ? Math.min : Math.max)(...rectangles.map(rect => rect[i])));
    for (let point of [[corners[0], corners[1]], [corners[0], corners[3]], [corners[2], corners[3]], [corners[2], corners[1]]]) {
        if (!set.delete(point.toString())) {
            return false;
        }
    }
    const area = rectangles.reduce((acc, rect) => acc + (rect[3] - rect[1]) * (rect[2] - rect[0]), 0);
    return area == (corners[3] - corners[1]) * (corners[2] - corners[0]);
};

