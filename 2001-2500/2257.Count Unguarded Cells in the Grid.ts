function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    const guardsSet = new Set(guards.map(cell => cell.toString()));
    const wallsSet = new Set(walls.map(cell => cell.toString()));
    const res = new Set();
    [guards, walls].forEach(cells => cells.forEach(cell => res.add(cell.toString())));

    const checkCell = (cellArr, isGuarded) => {
        const cell = cellArr.toString()
        if (guardsSet.has(cell)) {
            isGuarded = true;
        } else if (wallsSet.has(cell)) {
            isGuarded = false;
        } else if (isGuarded) {
            res.add(cell);
        }
        return isGuarded;
    }
    for (let i = 0; i < m; i++) {
        let isGuarded = false;
        for (let j = 0; j < n; j++) {
            isGuarded = checkCell([i, j], isGuarded);
        }
        isGuarded = false;
        for (let j = n - 1; j >= 0; j--) {
            isGuarded = checkCell([i, j], isGuarded);
        }
    }

    for (let j = 0; j < n; j++) {
        let isGuarded = false;
        for (let i = 0; i < m; i++) {
            isGuarded = checkCell([i, j], isGuarded);
        }
        isGuarded = false;
        for (let i = m - 1; i >= 0; i--) {
            isGuarded = checkCell([i, j], isGuarded);
        }
    }
    return m * n - res.size;
};

