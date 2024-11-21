#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
int characters[26] = { 0 };

int main(void)
{
	char ans[9];
	char input[9];
	int i=0,j,y=0,g=0;
	while (i < 9)
	{
		ans[i] = fgetc(stdin);
		if (ans[i] != '\n')
		{
			characters[ans[i] - 'A']++;
			i++;
			
		}
	}
	
	
	i = 0;
	while (i < 9)
	{
		input[i] = fgetc(stdin);
		if (input[i] != '\n')
			i++;
	}
	for (i = 0; i < 9; i++)
	{
		if (input[i] == ans[i])
		{
			g++;
			characters[ans[i] - 'A']--;
			input[i] = '0';
			
		}
	}
	
	for (i = 0; i < 9; i++)
	{
		if (input[i]!= '0' && characters[input[i]-'A'] > 0)
		{
			y++;
			characters[input[i]-'A']--;
		}
	}
	printf("%d\n%d", g, y);
	return 0;
}