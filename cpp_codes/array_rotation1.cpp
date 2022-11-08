//rotation of array using temporary array
#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int arr[n];
    for (int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    int d;
    cin>>d;
    int arr2[n];
    for (int i=d;i<n;i++){
        arr2[i-d]=arr[i];
    }
    for (int i=0;i<d;i++){
        arr2[n-d+i]=arr[i];
    }
    for (int i=0;i<n;i++)
    {
        cout<<arr2[i]<<" ";
    }
    return 0;
}