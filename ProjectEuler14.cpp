#include<iostream>
using namespace std;

int Collatz(long long int n){
	int res = 1;
	while(n!=1){
		if(n % 2 ==0){
			n = n/2;
		}else{
			n = 3*n+1;
		}
		res++;
	}
	return res;
}

int main (int argc, char *argv[]) {
	int i=2;
	int res = 0;
	int CadenaMasLarga = 0;
	for(int i = 2; i <= 1000000; i++){
		if(Collatz(i)>= CadenaMasLarga){
			CadenaMasLarga = Collatz(i);
			res = i;
		}
	}
	cout << res <<endl;
	return 0;
}

