class Student
{
int roll_no;
void getRoll(int r)
{
roll_no = r;
}
void showRoll()
{
System.out.println("Roll No: " + roll_no);
}
}
class Test extends Student
{
int sub1, sub2;
void getMarks(int m1, int m2)
{
sub1 = m1;
sub2 = m2;
}
void showMarks()
{
System.out.println("Marks: " + sub1 + ", " + sub2);
}
}
class Result extends Test
{
void displayResult()
{
int total = sub1 + sub2;
System.out.println("Total Marks: " + total);
}
}
class MultiLevelTest {
public static void main(String[] args)
{
Result r = new Result();
r.getRoll(101);
r.getMarks(80, 90);
r.showRoll();
r.showMarks();
r.displayResult();
}
}
