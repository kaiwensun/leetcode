int numberOfSubstrings(char * s){
    char *l = s, *r = s;
    int cnt = 0;
    int window[] = {0, 0, 0};
    while (*r != '\0') {
        window[*(r++) - 'a']++;
        while (window[0] > 0 && window[1] > 0 && window[2] > 0) {
            window[*(l++) - 'a']--;
        }
        cnt += r - l;
    }
    return (r - s) * (r - s + 1) / 2 - cnt;
}
