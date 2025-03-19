#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int suma(int a, int b){
	return a+b;
}
int resta(int a, int b){
	return a-b;
}

int main(){
	int length;
	scanf("%i", &length);

	int office = pow(2,length);
	printf("%i", office);
	return 0;
}