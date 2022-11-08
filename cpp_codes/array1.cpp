#include<iostream>
using namespace std;
int main(){
    int a[5]={1,2,3,4,5};
    cout<<a[6]<<"\n";
    cout<<a[-2]<<"\n";
    for (int i = 0; i < 5; i++){
        // The use of '&' before a variable name, yields
        // address of variable.
        cout << "Address arr[" << i << "] is " << &a[i]<< "\n";
        cout <<i[a]<<"\n";
    }
    return 0;
}