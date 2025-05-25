#include <iostream>
using namespace std;
int main()
{
    int a,b ;
    char op;

    cout<<"Enter the value of a : " ;
    cin>>a;

    cout<<"Enter the value of b : " ;
    cin>>b;

    cout<<"Enter the operator : " ;
    cin>>op;

//LOGIC FOR CALCULATOR
//use single quotes instead of double . In C++, a char type is enclosed in single quotes ('). 
if (op == '+') {
    cout << "a+b: " << (a + b) << endl;
} else if (op == '-') {
    cout << "a-b: " << (a - b) << endl;
} else if (op == '*') {
    cout << "a*b: " << (a * b) << endl;
} else if (op == '/') {
    cout << "a/b: " << (a / b) << endl;
} else {
    cout << "Invalid Operator" << endl;
}

return 0;
}





















