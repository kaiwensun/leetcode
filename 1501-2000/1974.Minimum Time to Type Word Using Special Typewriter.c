#define min(a,b) (a > b) ? (b) : (a);

int minTimeToType(char * word){
    char last = 'a';
    int res = 0;
    char* p;
    for (p = word; *p != '\0'; p++) {
        int step = (*p - last + 26) % 26;
        res += min(step, 26 - step);
        last = *p;
    }
    return p - word + res;
}

