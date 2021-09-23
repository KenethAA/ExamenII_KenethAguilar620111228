#include<iostream>
#include<string.h>

using namespace std;

main() {
	
 string ejemplo,convert;
 int val, i;
 
 ejemplo="ab-cd";

 
 val= ejemplo.length();
 
 
 for(i=val; i>=0; i--)
 {
 	convert = convert + ejemplo.substr(i, 1);
 }

cout<<"Invertido: "<<convert;

}
