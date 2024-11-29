#include <stdio.h>


int main(void) ///counting sort
{
	int n,array[10000],i,a,j,k;
	for (i = 0; i < 10000; i++)
		array[i] = 0;
	scanf("%d", &n);
	
	for (i = 0; i < n; i++)
	{
		scanf("%d", &a);
		array[a-1]++;
	}
	
	for (i = 0; i < 10000; i++)
	{
		k = array[i];
		
		for (j = 0; j < k; j++)
			printf("%d\n", i+1);
	}
	return 0;
}