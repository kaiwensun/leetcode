
int assigned[26]; // -1 means not assigned. otherwise, the assigned 0-9 value
bool is_leading[26]; // if the character is a lead letter, which means it can't be 0
int letters[10];
int letterCnt;
bool num_used[10];

char ** words;
int wordsSize;
char * result;

void init(char** w, int ws, char* r) {
    int i;
    words = w;
    wordsSize = ws;
    result = r;
    memset(assigned, -1, 26 * sizeof(int));
    memset(is_leading, false, 26 * sizeof(bool));
    memset(num_used, false, 10 * sizeof(bool));
    letterCnt = 0;
    int lettersFlag[26] = {};
    for (i = 0; i <= wordsSize; i++) {
        char* word = i == wordsSize ? result : words[i];
        is_leading[word[0] - 'A'] = true;
        for (char* p = word; *p; p++) {
            lettersFlag[*p - 'A'] = true;
        }
    }
    for (i = 0; i < 26; i++) {
        if (lettersFlag[i]) {
            letters[letterCnt++] = i;
        }
    }
}

bool isSolution() {
    int sum = 0;
    for (int i = 0; i < wordsSize; i++) {
        sum += word2num(words[i]);
    }
    sum -= word2num(result);
    return sum == 0;
}

int word2num(char* word) {
    int num = 0;
    while(*word) {
        num *= 10;
        num += assigned[*(word++) - 'A'];
    }
    return num;
}

bool backtrack(int index) {
    if (index == letterCnt) {
        return isSolution();
    }
    for (int val = 0; val < 10; val++) {
        if ((val == 0 && is_leading[letters[index]]) || num_used[val]) {
            continue;
        }
        num_used[val] = true;
        assigned[letters[index]] = val;
        if (backtrack(index + 1)) {
            return true;
        }
        num_used[val] = false;
    }
    return false;
}

bool quickFindNotEqual(char ** words, int wordsSize, char * result) {
    int maxLen = 0;
    for (int i = 0; i < wordsSize; i++) {
        int wordLen = strlen(words[i]);
        maxLen = maxLen > wordLen ? maxLen : wordLen;
    }
    return maxLen > strlen(result);
}

bool isSolvable(char ** words, int wordsSize, char * result) {
    if (quickFindNotEqual(words, wordsSize, result)) {
        return false;
    }
    init(words, wordsSize, result);
    return backtrack(0);
}
