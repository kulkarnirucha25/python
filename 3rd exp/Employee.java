class Employee 
{
String name, address, jobTitle;
double salary;
Employee(String n, String a, String j, double s)
{
name = n;
address = a;
jobTitle = j;
salary = s;
}
void calculateBonus()
{
System.out.println("Bonus: " + (salary * 0.10));
}
void performanceReport()
{
System.out.println(name + " performance is excellent.");
}
void manageProject()
{
System.out.println(name + " is managing a project.");
}
}
class Manager extends Employee
{
Manager(String n, String a, double s){
super(n, a, "Manager", s);
}
}
class Developer extends Employee
{
Developer(String n, String a, double s)
{
super(n, a, "Developer", s);
}
}
class Programmer extends Employee
{
Programmer(String n, String a, double s)
{
super(n, a, "Programmer", s);
}
}
class CompanyTest
{
public static void main(String[] args)
{
Manager m = new Manager("Ravi", "Pune", 60000);
Developer d = new Developer("Asha", "Mumbai", 50000);
Programmer p = new Programmer("Neha", "Delhi", 45000);
m.calculateBonus();
d.performanceReport();
p.manageProject();
}
}
