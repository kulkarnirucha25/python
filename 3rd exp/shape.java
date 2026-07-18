abstract class shape
{
double dim1,dim2;
shape(double d1,double d2)
{
dim1=d1;
dim2=d2;
}
abstract double area();
}
class rectangle extends shape
{
rectangle(double l,double b)
{
super(l,b);
}
double area()
{
return dim1*dim2;
}
}
class triangle extends shape
{
triangle(double b,double h)
{
super(b,h);
}
double area()
{
return 0.5*dim1*dim2;
}
}
class shapetest
{
public static void main(String[] args)
{
rectangle r= new rectangle(5,4);
triangle t=new triangle(6,3);
System.out.println("Area of Rectangle: "+r.area());
System.out.println("Area of Triangle: "+t.area());
}
}
