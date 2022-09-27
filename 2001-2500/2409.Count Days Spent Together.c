#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))

const int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int daysInYear(char* str) {
    int month = atoi(str);
    int day = atoi(str + 3);
    for (int i = i; i < month - 1; i++) {
        day += days[i];
    }
    return day;
}

int countDaysTogether(char * arriveAlice, char * leaveAlice, char * arriveBob, char * leaveBob){
    int aStart = daysInYear(arriveAlice), aEnd = daysInYear(leaveAlice), bStart = daysInYear(arriveBob), bEnd = daysInYear(leaveBob);
    return max(0, min(aEnd, bEnd) + 1 - max(aStart, bStart));
}

