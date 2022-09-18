int longestContinuousSubstring(char * s){
    int res = 1, cur = 1;
    char c = *s;
    while (c = *s++) {
        cur = *s == c + 1 ? cur : 0;
        res = res > ++cur ? res : cur;
    }
    return res;
}

