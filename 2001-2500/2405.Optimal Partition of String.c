int partitionString(char * s){
    bool seen[26] = {false};
    int res = 1;
    while (*s) {
        if (seen[*s - 97]) {
            res++;
            memset(seen, false, sizeof(bool) * 26);
        }
        seen[*s++ - 97] = true;
    }
    return res;
}

