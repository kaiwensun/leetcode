#define min(x,y) x<y?x:y
#define ZRO '0'
#define ONE '1'
struct Pix{
	int left;	//including self
	int up;		//including self
	int border_upleft;	//including self
};
int maximalSquare(char** matrix, int matrixRowSize, int matrixColSize) {
	if (matrixColSize <= 0 || matrixRowSize <= 0)
		return 0;
	int tmp = matrixRowSize; matrixRowSize = matrixColSize; matrixColSize = tmp;
	//new space
	struct Pix** pix = (struct Pix**)malloc(sizeof(struct Pix*)*matrixColSize);
	for (int i = 0; i < matrixColSize; i++)
	{
		pix[i] = (struct Pix*)malloc(sizeof(struct Pix)*matrixRowSize);
		memset(pix[i], -1, sizeof(struct Pix)*matrixRowSize);
	}
	//initinalizing
	int max_square_border = 0;
	for (int i = 0, left = 0; i < matrixRowSize; i++)
	{
		if (matrix[0][i] == ONE)
		{
			left++;
			pix[0][i].left = left;
			pix[0][i].up = 1;
			pix[0][i].border_upleft = 1;
			max_square_border = 1;
		}
		else
		{
			left = 0;
			pix[0][i].left = 0;
			pix[0][i].up = 0;
			pix[0][i].border_upleft = 0;

		}
	}
	for (int j = 0, up = 0; j < matrixColSize; j++)
	{
		if (matrix[j][0] == ONE)
		{
			up++;
			pix[j][0].left = 1;
			pix[j][0].up = up;
			pix[j][0].border_upleft = 1;
			max_square_border = 1;
		}
		else
		{
			up = 0;
			pix[j][0].left = 0;
			pix[j][0].up = 0;
			pix[j][0].border_upleft = 0;
		}
	}
	//fill table
	for (int i = 1; i < matrixColSize; i++)
	{
		for (int j = 1; j < matrixRowSize; j++)
		{
			if (matrix[i][j] == ONE)
			{
				pix[i][j].left = pix[i][j - 1].left + 1;
				pix[i][j].up = pix[i - 1][j].up + 1;
				int old_up_left = pix[i - 1][j - 1].border_upleft;
				if (pix[i][j].left>old_up_left && pix[i][j].up>old_up_left)
					pix[i][j].border_upleft = old_up_left + 1;
				else
					pix[i][j].border_upleft = min(pix[i][j].left, pix[i][j].up);
				if (pix[i][j].border_upleft > max_square_border)
					max_square_border = pix[i][j].border_upleft;
			}
			else
			{
				pix[i][j].left = 0;
				pix[i][j].up = 0;
				pix[i][j].border_upleft = 0;
			}
		}
	}
	return max_square_border*max_square_border;
}
