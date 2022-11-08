import java.util.HashMap;
import java.util.Map;

public class AddHashmap
{  
     public static void main(String args[]){  
       HashMap<String,String> map=new HashMap<String,String>();//Creating HashMap    
       map.put("Himanshu", "gupta");  //adding elements in Map  
       map.put("IIIT","Nagpur");    
       map.put("Rama","jangir");   
       map.put("Ruhi", "Mehta");   
           
       System.out.println("Hashmap ELements: ");  
       for(Map.Entry m : map.entrySet()){    
        System.out.println(m.getKey()+" "+m.getValue());    
       }  
       
       //To Check If A HashMap Is Empty Or Not
       System.out.println("Is Hashmap EMpty "+map.isEmpty());
    }  
}  