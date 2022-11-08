#include<iostream>
using namespace std;

int binarySearch(int arr[], int low, 
                 int high, int key) 
{ 
    if (high < low) 
        return -1; 
  
    int mid = (low + high) / 2; /*low + (high - low)/2;*/
    if (key == arr[mid]) 
        return mid; 
  
    if (key > arr[mid]) 
        return binarySearch(arr, (mid + 1), high, key); 
  
    // else 
    return binarySearch(arr, low, (mid - 1), key); 
} 

int pivot(int arr[], int f, int l)
{
    int mid=(f+l)/2;
    //cout<<"mid"<<mid<<"f "<<f<<"l "<<l<<endl;
    if(arr[mid]>=arr[f] && arr[mid]>=arr[l])
    {
        if((mid)==(l-1))
        {
            //cout<<"mid+1 "<<arr[mid]<<endl;                                                                         
            return mid;
        }
        else
        {
           // cout<<"return pivot(arr, mid, l)";
            return pivot(arr, mid, l);
        }
            
    }
    else if(arr[mid]<arr[f] && arr[mid]<arr[l])
    {
        //cout<<"pivot(arr, f, mid)";
        return pivot(arr, f, mid);
    }
    else
    {
            return -1;
    }

}
int pivotBinarySearch(int arr[], int n, int key)
{
    int pi=pivot(arr,0,n-1);
    //cout<<pi;
    if (pi == -1) 
        return binarySearch(arr, 0, n - 1, key); 
  
    // If we found a pivot, then first compare with pivot 
    // and then search in two subarrays around pivot 
    if (arr[pi] == key) 
        return pi; 
  
    if (arr[0] <= key) 
        return binarySearch(arr, 0, pi - 1, key); 
  
    return binarySearch(arr, pi + 1, n - 1, key); 
}
int main()
{
    int arr[]={ 5, 6, 7, 8, 9, 10, 1, 2, 3};;
    int key=3;
    int n=sizeof(arr)/sizeof(int);
    cout<<"element "<<key<<" is found at index: "<<pivotBinarySearch(arr, n, key)<<endl;
    
    return 0;
}