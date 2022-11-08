//A Juggling Algorithm
/*Instead of moving one by one, divide the array in different sets
where number of sets is equal to GCD of n and d and move the elements within sets*/

#include<iostream>
using namespace std;
int gcd(int a,int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}

void leftrotate(int arr[], int n, int d)
{
    d=d%n;
    int j, k;
    for (int i=0;i<gcd(d,n);i++)
    {
        int temp=arr[i];
        j=i;
        while(true)
        {
            k=j+d;
            if(k>=n)
                k-=n;

            if(k==i)
                break;

            arr[j]=arr[k];
            j=k;

        }
        arr[j]=temp;
    }
}
int main()
{
    int arr[]={1,2,3,4,5,6,7};
    int n=sizeof(arr)/sizeof(int);
    leftrotate(arr,n,2);
    for (int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    return 0;
}