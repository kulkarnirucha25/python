class Employee {
private String firstName;
private String lastName;
private double monthlySalary;

Employee(String f, String l, double salary) {
firstName = f;
lastName = l;
if (salary > 0)
   monthlySalary = salary;
else
   monthlySalary = 0.0;
}
void setFirstName(String f) {
  firstName = f;
}
void setLastName(String l) {
lastName = l;
}
void setMonthlySalary(double salary) {
if (salary > 0)
  monthlySalary = salary;
else
  monthlySalary = 0.0;
}
String getFirstName() {
return firstName;
}
String getLastName() {
return lastName;
}
double getMonthlySalary() {
 return monthlySalary;
}
double getYearlySalary() {
 return monthlySalary * 12;
}
}

public class EmployeeTest {
 public static void main(String[] args) {

Employee emp1 = new Employee("Rucha", "Kulkarni", 25000);
Employee emp2 = new Employee("Amit", "Patil", 30000);

System.out.println("Yearly Salary of Employee 1: " + emp1.getYearlySalary());
System.out.println("Yearly Salary of Employee 2: " + emp2.getYearlySalary());

emp1.setMonthlySalary(emp1.getMonthlySalary() * 1.10);
emp2.setMonthlySalary(emp2.getMonthlySalary() * 1.10);

System.out.println("\nAfter 10% Raise:");
System.out.println("Yearly Salary of Employee 1: " + emp1.getYearlySalary());
System.out.println("Yearly Salary of Employee 2: " + emp2.getYearlySalary());
}
}
