function* fibGenerator(): Generator<number, any, number> {
    let a = -1, b = 1;
    while (true) {
        [a, b] = [b, a + b];
        yield b;
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */

