//Block swap algorithm for array rotation
#include<iostream>
using namespace std;
void swap(int arr[], int f, int l, int d)
{
    int tmp;
    for (int i=0;i<d;i++)
    {
        tmp=arr[f+i];
        arr[f+i]=arr[l+i];
        arr[l+i]=tmp;
    }
}
void leftrotate(int arr[], int n, int d)
{
    if(d == 0 || d == n)
        return;
    if(n-d == d)
    {
        swap(arr, 0, n-d, d);
       /* cout<<"d=n-d ";
        for (int i=0;i<n;i++)
            cout<<arr[i]<<" ";
        cout<<endl;*/
        return;   
    }
    if(d < n-d)
    {
        swap(arr, 0, n-d, d);
       /* cout<<"d<n-d ";
        for (int i=0;i<n;i++)
            cout<<arr[i]<<" ";
        cout<<endl;*/
        leftrotate(arr, n-d, d);
    }
    else
    {
        swap(arr, 0, d, n-d);
        /*cout<<"d>n-d ";
        for (int i=0;i<n;i++)
            cout<<arr[i]<<" ";
        cout<<endl;*/
        leftrotate(arr+n-d, d, 2*d-n);
    }
    
}
int main()
{
    int arr[]={1,2,3,4,5,6,7};
    int n=sizeof(arr)/sizeof(int);
    leftrotate(arr,n,2);
    for (int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}