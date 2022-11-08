class Teacher {
   String designation = "Head of Department";
   String college = "IIIT Nagpur";
   void does(){
	System.out.println("Managing the teacher");
   }
}
class MathTeacher extends Teacher{
   String mainSubject = "Maths";
   
}
public class InheritTeacher {
    public static void main(String args[]){
      MathTeacher obj = new MathTeacher();
      System.out.println(obj.college);
      System.out.println(obj.designation);
      System.out.println(obj.mainSubject);
      obj.does();
   }
}
