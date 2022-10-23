function haveConflict(event1: string[], event2: string[]): boolean {
    function toMinutes(time: string) {
        return parseInt(time.substring(0, 2)) * 60 + parseInt(time.substring(3, 5));
    }
    return Math.min(toMinutes(event1[1]), toMinutes(event2[1])) >= Math.max(toMinutes(event1[0]), toMinutes(event2[0]))
};

