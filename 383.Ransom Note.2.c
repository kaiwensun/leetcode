bool canConstruct(char * ransomNote, char * magazine){
    int counter[26] = {0};
    while(*magazine) counter[*magazine++ - 'a']++;
    while(*ransomNote) counter[*ransomNote++ - 'a']--;
    for (int i = 0; i < 26; i++)
        if (counter[i] < 0) return false;
    return true;
}
