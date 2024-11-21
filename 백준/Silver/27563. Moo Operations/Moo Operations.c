#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int count;
int len;
int shape;
int compare(int index,char* s)
{
	
	if (s[index] == 'O')
	{
		if (s[index + 1] == 'O')
		{
			if (s[index + 2] == 'O')
				return 1;
			else if(s[index + 2] == 'M')
				return 4;
		}
	}
	else if (s[index] == 'M')
	{
			if (s[index + 1] == 'O')
			{
				if (s[index + 2] == 'M')
					return 2;
				else if (s[index + 2] == 'O')
					return 3;
			}
	}
	return -1;
	
}
int search(char* s,int n)
{
	int i;
	i = 0;
	while (i < n - 2)
	{
		int k = compare(i, s);

		if (k == 1) ///OOO
		{
			if (shape < 2)
				shape = 2;
		}
		else if (k == 2) ///MOM
		{
			if (shape < 2)
				shape = 2;
		}
		else if (k == 3) ///MOO
		{
			if (shape < 3)
				shape = 3;
		}
		else if (k == 4)
		{
			if (shape < 1)
				shape = 1;
		}
		i++;
	}
	if (shape == 1)
	{
		count += len - 1;
		return 1;
	}
	else if (shape == 2)
	{
		count+=len - 2;
		return 2;
	}
	else if (shape == 3)
	{
		count += len - 3;
		return 3;
	}
	else
		return -1;
}

int main(void)
{
	int	NumOfString;
	scanf("%d", &NumOfString);
	char string[101];
	for (int i = 0; i < NumOfString; i++)
	{
		count = 0;
		shape = 0;
		scanf("%s", string);
		len = strlen(string);
		int k = search(string, len);
		if (len >= 3)
		{
			if (k == 1) ///OOO
			{
				printf("%d\n", count);
			}
			else if (k == 2) ///MOM
			{
				printf("%d\n", count);
			}
			else if (k == 3) //MOO
			{
				printf("%d\n", count);
			}
			else
				printf("-1\n");
		}
		else printf("-1\n");
	}

	return 0;
}