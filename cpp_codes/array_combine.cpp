/*Given two sorted arrays A and B, generate all possible arrays such that first element is taken from A then from B then from A and so on in increasing order till the arrays exhausted. The generated arrays should end with an element from B.
*/
#include<iostream>
using namespace std;

void printArr(int arr[], int n)
{
    for (int i=0;i<n;i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}

/* Function to generates and prints all sorted arrays from alternate elements of 
   'A[i..m-1]' and 'B[j..n-1]' 
   If 'flag' is true, then current element is to be included from A otherwise 
   from B. 
   'len' is the index in output array C[]. We print output  array  each time 
   before including a character from A only if length of output array is 
   greater than 0. We try than all possible combinations */
void generateall(int a[], int b[], int c[],int i, int j, int n, int m, int len, bool flag )
{
    if(flag) // Include valid element from A 
    {
        // Print output if there is at least one 'B' in output array 'C' 
        if(len)
            printArr(c,len+1);
        
         // Recur for all elements of A after current index 
        for(int k=i;k<n;k++)
        {
            if(!len)
            {
                /* this block works for the very first call to include 
                     the first element in the output array */
                c[len]=a[k];
                cout<<"A+ flag+not len "<<c[len]<<endl;
                 // don't increment lem as B is included yet 
                generateall(a,b,c,k+1,j,n,m,len,!flag);
            }
            else    /* include valid element from A and recur */
            {
                if(a[k]>c[len])
                {
                    c[len+1]=a[k];
                    cout<<"A+ flag+len "<<c[len+1]<<endl;
                    generateall(a,b,c, k+1, j, n, m, len+1, !flag);
                }

            }
            
        }
    }
    else    /* Include valid element from B and recur */
    {
        for(int l=j;l<m; l++)
        {
            if(b[l]>c[len])
            {
                c[len+1]=b[l];
                cout<<"B+not flag "<<c[len+1]<<endl;
                generateall(a,b,c,i, l+1, n, m, len+1, !flag);
            }
        }
    }
    
}
void generate(int a[],int b[], int n,int m)
{
    int c[n+m]; //output array
   
    generateall(a,b,c,0,0,n,m,0,true);
    
}

int main()
{
    int A[] = {10, 15, 25}; 
    int B[] = {5, 20, 30}; 
    int n = sizeof(A)/sizeof(A[0]); 
    int m = sizeof(B)/sizeof(B[0]); 
    generate(A, B, n, m); 
    return 0; 
}
