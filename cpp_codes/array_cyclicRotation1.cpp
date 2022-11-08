#include<iostream>
using namespace std;
void cyclicRotate(int arr[], int n)
{
    if(d==0)
        return;
    int tmp=arr[n-1];
    int i;
    for (i=n-1;i>0;i--)
    {
        arr[i]=arr[i-1];
    }
    arr[i]=tmp;
}
int main()
{
    int arr[]={1,2,3,4,5};
    int n=sizeof(arr)/sizeof(int);
    cyclicRotate(arr,n);
    for (int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}