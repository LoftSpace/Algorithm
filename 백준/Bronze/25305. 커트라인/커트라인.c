#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int n, k,*arr,i;
	int j, dummy;
	scanf("%d", &n);
	scanf("%d", &k);
	arr = (int*)malloc(sizeof(int) * n);
	for (i = 0; i < n; i++)
		scanf("%d", &arr[i]);
	for (i = 0; i < n; i++)
	{
		dummy = arr[i];
		j = i;
		while (arr[j - 1] > dummy&& j > 0)
		{
			arr[j] = arr[j - 1];
			j--;
		}
		arr[j] = dummy;
	} //정렬
	printf("%d", arr[n-k]);
	free(arr);
    return 0;
}