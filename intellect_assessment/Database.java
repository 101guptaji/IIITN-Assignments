import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
public class Database {
   public static void main(String args[]) throws SQLException {
      String mysqlUrl = "jdbc:mysql://localhost/";
       DriverManager.registerDriver(new com.mysql.jdbc.Driver());
      System.out.println("Connecting to a selected database...");
      Connection con = DriverManager.getConnection(mysqlUrl, "username", "password");
      System.out.println("Connected database successfully...");
      Statement stmt = con.createStatement();
      String query = "CREATE database db";
      stmt.execute(query);
      System.out.println("Creating table in given database...");
      String sql="CREATE TABLE employee"+
                    "(EmpName varchar(255) not NULL,"+
                    "id int not NULL,"+
                    "Dept varchar(255) not NULL"+
                    "PRIMARY KEY (id))";


      
      stmt = con.createStatement();
      stmt.execute(sql);


      sql= "INSERT INTO employee"+
            "(ROLL_NO, NAME, AGE, CITY)"+
            "VALUES (1,'Rakshita','abc')";
        stmt = con.createStatement();
      stmt.execute(sql);

      sql= "INSERT INTO employee"+
            "(ROLL_NO, NAME, AGE, CITY)"+
            "VALUES (2,'Tarkeshwar','abc')";
        stmt = con.createStatement();
      stmt.execute(sql);

      sql= "INSERT INTO employee"+
            "(ROLL_NO, NAME, AGE, CITY)"+
            "VALUES (3,'Naveen','abc')";
        stmt = con.createStatement();
      stmt.execute(sql);


      
   }
}