function passThePillow(n: number, time: number): number {
    time %= (n - 1) * 2;
    return Math.min(time, (n - 1) * 2 - time) + 1;
};

