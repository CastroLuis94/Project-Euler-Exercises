#include<iostream>
using namespace std;

int MultiplosHasta(int n,int limite){
	int i = 1;
	int res = 0;
	while(n*i < limite){
		res += n*i;
		i++;
	}
	return res;
}

int main (int argc, char *argv[]) {
	
	int multiplosDeTres = MultiplosHasta(3,1000);
	int multiplosDeCinco = MultiplosHasta(5,1000);
	int multiplosDeQuince = MultiplosHasta(15,1000);
	int res = multiplosDeTres+multiplosDeCinco-multiplosDeQuince;
	cout << res <<endl;
	return 0;
}

