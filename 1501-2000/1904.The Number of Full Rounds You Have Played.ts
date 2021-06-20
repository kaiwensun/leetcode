function numberOfRounds(startTime: string, finishTime: string): number {
        const getMinute = (time:string):number => parseInt(time.slice(0, 2)) * 60 + parseInt(time.slice(3));
        const ROUND = 15;
        return (Math.floor(getMinute(finishTime) / ROUND) - Math.ceil(getMinute(startTime) / ROUND) + 24 * 4) % (24 * 4);
};

