#include <stdio.h>
#include <stdlib.h>  ///merge sort 는 2개로 놔뉨: 분할정복:devide and conquer

#define MAX 500000

int count = 0;

void merge(int* a, int l, int q, int r,int k)  ///conquer
{
	int i = l;
	int j = q+1;
	int t = 1;
	int f=0;
	int temp[MAX];
	while (i <= q && j <= r)
	{
		if (a[i] >= a[j])
		{
			temp[f++] = a[j++];
			count++;
			if (count == k)
				printf("%d", temp[--f]);
		}
		else
		{
			temp[f++] = a[i++];
			count++;
			if (count == k)
				printf("%d", temp[--f]);
		}
	}
	while (i <= q)
	{
		temp[f++] = a[i++];
		count++;
		if (count == k)
			printf("%d", temp[--f]);
	}
	while (j <= r)
	{
		temp[f++] = a[j++];
		count++;
		if (count == k)
			printf("%d", temp[--f]);
	}
	for (int y = l; y <= r; y++)
		a[y] = temp[y-l];
}
void merge_sort(int* a,int l,int r,int k) ///devide
{
	if (r > l)
	{
		int q = l + (r-l)/2;  ////(l+r)/2랑 똑같은데 이렇게하면 오버플로우 방지할수 있음
		merge_sort(a, l, q,k);
		merge_sort(a, q + 1, r,k);
		merge(a, l, q, r,k);
	}
}

int main(void)
{
	int N,k,n;
	int i;
	scanf("%d %d", &N,&k);
	int* A = (int*)malloc(sizeof(int) * N);
	for (i = 0; i < N; i++)
	{
		scanf(" %d", &A[i]);
		
	}
	
	merge_sort(A, 0, N-1,k);
	if (k > count)
		printf("-1");
	
	return 0;

}