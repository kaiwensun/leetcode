#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include<math.h>
/*
void rotate(int** matrix, int matrixRowSize, int matrixColSize) {
	int n = matrixRowSize;
	if (n == 0 || n == 1)
		return;
	for (int i = 0; i < n / 2; i++)
	{
		for (int j = 0; j < n / 2; j++)
		{
			int tmp = matrix[i*n+j];
			matrix[i*n+j] = matrix[(n - j - 1)*n+i];
			matrix[(n - j - 1)*n+i] = matrix[(n - i - 1)*n+(n - j - 1)];
			matrix[(n - i - 1)*n+(n - j - 1)] = matrix[j*n+(n - i - 1)];
			matrix[j*n+(n - i - 1)] = tmp;
		}
	}
	if (n % 2 == 1)
	{
		int mid = n / 2;
		for (int i = 0; i < n/2; i++)
		{
			int tmp = matrix[mid+n*i];
			matrix[mid+n*i] = matrix[i+n*mid];
			matrix[i+n*mid] = matrix[mid+n*(n - i - 1)];
			matrix[mid+n*(n - i - 1)] = matrix[(n - i - 1)+n*mid];
			matrix[(n - i - 1)+n*mid] = tmp;
		}
	}
}
*/
void rotate(int** matrix, int matrixRowSize, int matrixColSize) {
	int n = matrixRowSize;
	if (n == 0 || n == 1)
		return;
	for (int i = 0; i < n / 2; i++)
	{
		for (int j = 0; j < n / 2; j++)
		{
			int tmp = matrix[i][j];
			matrix[i][j] = matrix[(n - j - 1)][i];
			matrix[(n - j - 1)][i] = matrix[(n - i - 1)][(n - j - 1)];
			matrix[(n - i - 1)][ + (n - j - 1)] = matrix[j][(n - i - 1)];
			matrix[j][ + (n - i - 1)] = tmp;
		}
	}
	if (n % 2 == 1)
	{
		int mid = n / 2;
		for (int i = 0; i < n / 2; i++)
		{
			int tmp = matrix[i][mid];
			matrix[i][mid] = matrix[mid][i];
			matrix[mid][i] = matrix[(n - i - 1)][mid];
			matrix[(n - i - 1)][mid] = matrix[mid][(n - i - 1)];
			matrix[mid][(n - i - 1)] = tmp;
		}
	}
}
void showPic(int** matrix, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			printf("%d", matrix[i*n+j]);
		printf("\n");
	}
}
int main()
{
	int pic[4][4] = { 1, 2, 3, 4, 5, 6, 7, 8, 90,0,0,0,0,0,0};
	showPic(pic, 4);
	rotate(pic, 4, 4);
	showPic(pic, 4);
	return 0;
}