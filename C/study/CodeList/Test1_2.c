#include <stdio.h>


void jolly();
void deny();

int main(void)  //��ϰ����ʹ��
{
	jolly();
	jolly();
	jolly();
	deny();

	return 0;
}

void jolly()
{
	printf("For he's a jolly good fellow!\n");

	return 0;
}
void deny()
{
	printf("which nobody can deny!\n");

	return 0;
}