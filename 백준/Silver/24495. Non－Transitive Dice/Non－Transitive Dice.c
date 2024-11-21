#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
int comp(int a[], int b[])
{

	int countA = 0, countB = 0,i,j;
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			if (a[i] > b[j])
				countA++;
			else if (a[i] < b[j])
				countB++;
		}
	}
	
	if (countA > countB)
		return 1;
	else
		return 0;
}

int main(void)
{
	int a[4], b[4], c[4];
	int i, j, n, k = 0;
	scanf("%d", &n); ///test case 개수
	int* ans = (int*) malloc(sizeof(int) * n);
	int check ;
	for (int u = 0; u < n; u++) 
	{
		
		check = 0; ///a vs b확인
		for (i = 0; i < 4; i++)
			scanf("%d", &a[i]);
		for (i = 0; i < 4; i++)
			scanf("%d", &b[i]);
		
		if (comp(a, b) == 1)
			check = 1;
		for(c[0]=1;c[0]<=10;c[0]++)
			for (c[1] = 1; c[1] <= 10; c[1]++)
				for (c[2] = 1; c[2] <= 10; c[2]++)
					for (c[3] = 1; c[3] <= 10; c[3]++)
					{
						if (check == 1)  ///a>b
						{

							if (comp(c, a) == 1) ///c>a
								if (comp(b, c) == 1) ///b>c
									ans[u] = 1;/// c가존재한다

						}
						else   ///a<b
						{
							if (comp(c, b) == 1) ///b<c
								if (comp(a, c) == 1) ///c<a
									ans[u] = 1;///c가 존재한다
						}
					}	
	}
	for (i = 0; i < n; i++)
	{
		if (ans[i] == 1)
			printf("yes\n");
		else
			printf("no\n");
	}
	return 0;
}