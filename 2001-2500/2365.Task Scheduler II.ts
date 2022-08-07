function taskSchedulerII(tasks: number[], space: number): number {
    const workedAt: {[key : number]: number} = {};
    let day = 0;
    tasks.forEach(task => {
        const taskWorkedAt = workedAt[task] || -Infinity;
        day = Math.max(day, taskWorkedAt + space) + 1;
        workedAt[task] = day;
    });
    return day;
};

