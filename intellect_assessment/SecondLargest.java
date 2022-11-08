public class SecondLargest{  
public static int get2nd(int[] a, int size){  
int tmp;  
//sorting of array
for (int i = 0; i < size; i++)   
        {  
            for (int j = i + 1; j < size; j++)   
            {  
                if (a[i] > a[j])   
                {  
                    //swaping of elements
                    tmp = a[i];  
                    a[i] = a[j];  
                    a[j] = tmp;  
                }  
            }  
        }  
        return a[size-2]; //return 2nd last element 
}  
public static void main(String args[]){  
int a[]={3,5,72,2,33,45,12};    
System.out.println("Second Largest: "+get2nd(a,7));    
}}  