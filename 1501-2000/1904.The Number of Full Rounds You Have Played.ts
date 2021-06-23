function numberOfRounds(startTime: string, finishTime: string): number {
        const getMinute = (time:string):number => parseInt(time.slice(0, 2)) * 60 + parseInt(time.slice(3));
        const ROUND = 15;
        const start = getMinute(startTime);
        const end = getMinute(finishTime);
        const startRound = Math.ceil(start / ROUND);
        const endRound = Math.floor(end / ROUND);
        if (startRound === endRound + 1 && start <= end) {
            return 0;
        }
        return (endRound - startRound + 24 * 4) % (24 * 4);
};

