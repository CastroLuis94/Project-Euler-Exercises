#include<iostream>
using namespace std;

int main (int argc, char *argv[]) {
	int i=2;
	long long int resto = 600851475143; 
	int res;
	while(i<=resto){
		if(resto % i == 0){
			resto = resto/i;
			res = i;
		}else{
			i++;
		}
	}
	cout << res <<endl;
	return 0;
}

