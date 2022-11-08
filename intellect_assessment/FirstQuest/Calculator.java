package FirstQuest;

import java.util.Scanner;
public class Calculator {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    System.out.println("Enter any operation like (+,-,*,/)");
    String operator = in.next();

    System.out.print("Enter left and right operands: ");

    // nextDouble() reads the next double from the keyboard
    double left = in.nextDouble();
    double right = in.nextDouble();

    System.out.printf(left+" "+ operator+" "+right+ "= " );

    double result;

    switch (operator) {
      case "+":
        result = left + right;
        break;

      case "-":
        result = left - right;
        break;

      case "*":
        result = left * right;
        break;

      case "/":
        result = left/right;
        break;

      // operator doesn't match any case constant (+, -, *, /)
      default:
        System.out.printf("Invalid Operation");
        return;
    }

    System.out.println(result);
  }
}