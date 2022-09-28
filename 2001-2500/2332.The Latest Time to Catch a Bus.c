#include<stdlib.h>

int compare(int* a, int* b) { return *a - *b;}

int latestTimeCatchTheBus(int* buses, int busesSize, int* passengers, int passengersSize, int capacity){
    qsort(buses, busesSize, sizeof(*buses), compare);
    qsort(passengers, passengersSize, sizeof(*passengers), compare);
    int* pp = passengers;
    int res = *buses;
    for (int* bp = buses; bp < buses + busesSize; bp++) {
        int i;
        for (i = 0; i < capacity && pp < passengers + passengersSize && *pp <= *bp; i++, pp++) {
            if (pp == passengers || *(pp - 1) != *pp - 1) {
                res = *pp - 1;
            }
        }
        if (i != capacity && (pp == passengers || *(pp - 1) != *bp)) {
            res = *bp;
        }
    }
    return res;
}

