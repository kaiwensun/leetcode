bool detectCapitalUse(char * word){
    if (*(word + 1) == '\0') return true;
    bool isCap = *(word + 1) < 'a';
    if (isCap && *word >= 'a') return false;
    char* p = word + 2;
    while (*p) if (*p++ < 'a' ^ isCap) return false;
    return true;
}
