#include<iostream>
#include<vector>
using namespace std;

int SumaGaus( int n){
	return (n*(n+1)/2);
}	
int	Divisores(int n){
	int i = 2;
	int PotenciaDivisores = 1;
	int res = 1;
	int original = n;
	while(i <= n){
		if(n % i == 0){
			while(n % i ==0){
				PotenciaDivisores++;
				n = n/i;
			}
			res*=PotenciaDivisores;
			PotenciaDivisores = 1;
		}
		i++;
	}
	return res;
}
	
int main (int argc, char *argv[]) {
	int i = 1;
	int res = 1;
	while(Divisores(SumaGaus(i)) < 500){
		i++;
	}
	cout << SumaGaus(i) <<endl;
	return 0;
}

