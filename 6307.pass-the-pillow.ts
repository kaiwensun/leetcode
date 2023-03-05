function passThePillow(n: number, time: number): number {
    time %= ((n - 1) * 2);
    return (time < n ? time : (n - 1) - (time - (n - 1))) + 1;
};

