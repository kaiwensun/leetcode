#define max(x,y) ((x)>(y))?(x):(y)
#define min(x,y) ((x)<(y))?(x):(y)
char* longestPalindrome(char* s);
char* retrieveString(char* expds, int* dp, int max_center);
int* getDpTable(int len);
char* preprocess(char* s, int len);

char* longestPalindrome(char* s) {
	int len = strlen(s);
	char* expds = preprocess(s, len);
	int* dp = getDpTable(len);

	int base = 0;
	int explorer = 0;
	dp[0] = 0;  //half size of palindromic substring. center excluded.
	int max_center = 0;

	int newbase = 1;
	for (newbase = 1; expds[newbase] != '\0'; newbase++){
		int mirrorId = (base << 1) - newbase;
		if (newbase >= explorer || newbase + dp[mirrorId] >= explorer){
			//if such, then there is potential that we can explore more rightwards.
			int l, r;
			if (newbase >= explorer){
				l = newbase - 1;
				r = newbase + 1;
			}
			else{
				l = max((newbase << 1) - explorer, newbase - dp[mirrorId]) - 1;
				r = min(explorer, newbase + dp[mirrorId]) + 1;
			}
			while (expds[r] != '\0' && l>= 0 && expds[r] == expds[l]){
				r++;
				l--;
			}
			int newexplorer = r - 1;
			if (newexplorer != explorer){  //explorer is updated
				base = newbase;
				explorer = newexplorer;
			}
			dp[newbase] = newexplorer - newbase;
			//update center of longest palindrom
			max_center = dp[max_center]<dp[newbase] ? newbase: max_center;
		}
		else{
			dp[newbase] = dp[mirrorId];
		}
	}
	char* res = retrieveString(expds, dp, max_center);
	free(dp);
	free(expds);
	return res;

}
char* retrieveString(char* expds, int* dp, int max_center){
	int halflen = dp[max_center];
	char* rtn = NULL;
	rtn = (char*)malloc(sizeof(char)*(halflen + 1));
	if (rtn == NULL)return NULL;
	char* src = (expds[max_center] == '#') ? (expds + max_center - halflen) : (expds + max_center - halflen);
	char* dst = rtn;
	for (int i = 0; i<halflen; i++){
		src++;
		*dst++ = *src++;
	}
	*dst = '\0';
	return rtn;
}
int* getDpTable(int len){
	return (int*)malloc(sizeof(int)*((len << 1) + 1));
}
char* preprocess(char* s, int len){
	char* rtn = (char*)malloc(sizeof(char)*((len + 1) << 1));
	if (rtn == NULL){
		return NULL;
	}
	char* dst = rtn;
	while (*s != '\0'){
		*dst++ = '#';
		*dst++ = *s++;
	}
	*dst++ = '#';
	*dst++ = '\0';
	return rtn;
}
