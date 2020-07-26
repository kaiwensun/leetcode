#define minimum(x,y) x<y?x:y;
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
	int area1 = (C - A)*(D - B);
	int area2 = (G - E)*(H - F);
	int min_up = minimum(D, H);
	int min_down = minimum(-B, -F); min_down = -min_down;
	int min_left = minimum(-A, -E); min_left = -min_left;
	int min_right = minimum(C, G);
	if (min_up - min_down <= 0 || min_right - min_left <= 0)
		return area1 + area2;
	return -(min_up - min_down)*(min_right - min_left) + area1 + area2;
}

