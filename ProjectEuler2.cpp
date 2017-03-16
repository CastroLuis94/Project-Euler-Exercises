#include<iostream>
using namespace std;

int Fibbo(int n){
	if(n==0 or n==1){
		return 1;
	}else{
		int actual = 1;
		int avanzar = 1;
		int siguiente;
		int i=1;
		while(i<n){
			siguiente = actual+avanzar;
			avanzar = actual;
			actual = siguiente;
			i++;
		}
		return siguiente;
	}
}

int main (int argc, char *argv[]) {
	
	int i=0;
	int res = 0;
	while(Fibbo(i)<4000000){
		if(Fibbo(i)%2 ==0) res += Fibbo(i);
		i++;
	}
	cout << res <<endl;
	return 0;
}

