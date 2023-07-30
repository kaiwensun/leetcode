function numberOfEmployeesWhoMetTarget(hours: number[], target: number): number {
    return hours.filter(h => h >= target).length;
};

