/*
 *Result:
 *  126 / 126 test cases passed.
 *  Status: Accepted
 *  Runtime: 8 ms
 *Date:
 *  8/15/2016
 */
bool canConstruct(char* ransomNote, char* magazine) {
    int table[26]={0};
    for(char* c = magazine;*c!='\0';c++){
        table[*c-'a']++;
    }
    for(char* c = ransomNote;*c!='\0';c++){
        table[*c-'a']--;
        if(table[*c-'a']<0)
            return false;
    }
    return true;
}
