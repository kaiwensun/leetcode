#define MAX(x, y) (((x) > (y)) ? (x) : (y))

int lengthOfLongestSubstring(char * s){
    int cnt[256] = {0};
    int res = 0;
    for (char* r = s, *l = s; *r != '\0'; r++) {
        if (++cnt[*r] == 2) {
            while (cnt[*r] == 2) {
                cnt[*(l++)]--;
            }
        }
        res = MAX(res, r - l + 1);
    }
    return res;
}
