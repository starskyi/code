#include <stdio.h>

int main(void)   //ʹ��ʮ�����ƣ��˽��Ʒֱ��ӡ100
{
	int num = 100;
	printf("ʮ����num = %d, �˽���num = %o, ʮ������num = %x", num, num, num);
	printf("ʮ����num = %d, �˽���num = %#o, ʮ������num = %#x", num, num, num);

	return 0;
}