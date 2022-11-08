package FirstQuest;
class Addition
{
    void add(double num1, double num2)
    {
        double result=num1+num2;
        System.out.println("Sum of two numbers: "+ result);
    }
    void add(double num1, double num2, double num3)
    {
        Double result=num1+num2+num3;
        System.out.println("Sum of three numbers: "+ result);
    }
    void add(double num1, double num2, double num3, double num4)
    {
        Double result=num1+num2+num3+num4;
        System.out.println("Sum of four numbers: "+ result);
    }
}
public class MethodOverloading {
    public static void main(String[] args) 
    {    
    	Addition obj = new Addition();
        
        //For 2 numbers
        obj.add(10, 20);

        //For 3 numbers
        obj.add(15,15.8,12.0);
        
        //For 4 numbers
       obj.add(16.0,1,15.9,22.0);
    }
}
