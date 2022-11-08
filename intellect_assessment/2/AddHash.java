//program to add elements to HashSet
import java.util.HashSet;   //For Hashset and Iterator
public class AddHash {  
 public static void main(String args[]){  
  //Creating HashSet and adding elements  
    HashSet<String> set=new HashSet();  
           set.add("Ramu");    
           set.add("Manu");    
           set.add("Ravi");   
           set.add("Ramu");  
           set.add("BHagya");  

           System.out.println("Hashset Elements: "+set);

           //Hashset element to array
           String harray[]= new String[set.size()];
           set.toArray(harray);

           for(String tmp:harray){
               System.out.println(tmp);
           }
           
 }  
}
