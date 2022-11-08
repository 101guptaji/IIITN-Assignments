public class Duplicate {  
        public static void main(String[] args) {  
        String str1 = "i love to eat apple";  

        char str[] = str1.toCharArray();  
            
        System.out.printf("Duplicate characters are: ");  
        for(int i = 0; i <str.length; i++) {  
              
            for(int j = i+1; j <str.length; j++) {  
                if(str[i] == str[j] && str[i] != ' ') //check for duplicate charater except space.
                {  
                    System.out.print(str[j]+" ");
                    break;
                }  
            }  
        }
    }  
}   