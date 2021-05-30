int countGoodSubstrings(char * s){
    int len = strlen(s);
    int res = 0;
    for (int i = 0; i < len - 2; i++) {
        if (s[i] != s[i + 1] && s[i] != s[i + 2] && s[i + 1] != s[i + 2]) res++;
    }
    return res;
}

