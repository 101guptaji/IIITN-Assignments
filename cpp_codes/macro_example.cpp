#include<iostream>
//macro definition
#define limit 5
//macro with argument
#define area(l,b) (l*b)
int main()
{
    int l=2;
 for(int i=1;i<limit;i++){
     int area=area(l,i);
     std::cout<<"area is: "<<area<<std::endl;
 }
 return 0;
}
