# to print naturals numbers up to n 
# for loop
# n=int(input("Enter a number: "))
# for i in range(n):
#     print(i+1)
# else:
#     print("Naturals nos printed successfully")    

#to print even numbers upt o n
# n=int(input("Enter number: "))
# for i in range(n):
#     if i%2==0:
#         print(i)
#     else:
#         pass  

# to print odd numbers up to n  
# n=int(input("Enter number: "))
# for i in range(n):
#     if i%2!=0:
#         print(i)
#     else:
#         pass 

# program that prints 1 2 4 8 16 32....
# n=int(input("Enter number:"))
# for i in range (n):
#     print(2**i)

# sum the given sequence 1+1/1!+1/2!...+1/n!
# n=int(input("Enter number:"))
# sum=0
# fact=1
# for i in range (1,n+1):
#     fact=fact*i
#     sum=sum+(1/fact)
# sum=1+sum
# print("sum of the sequence is: ",sum)

#to print the cosine series cos(x)=1−x^2/2!+x^4/4!−x^6/6!+...
# n = int(input("Enter highest even power: "))
# x = float(input("Enter value of x: "))

# sum = 1
# sign = -1

# for i in range(2, n + 1, 2):
#     fact = 1

#     for j in range(1, i + 1):
#         fact = fact * j

#     term = (x ** i) / fact
#     sum = sum + (term * sign)
#     sign = sign * -1
#print("cos(x) =", sum)

#A B C
#A B C
#A B C
# for i in range(1,4):
#     for j in range(1,4):
#         if j==1:
#             print("A",end=" ")
#         elif j==2:
#             print("B",end=" ")    
#         else:
#             print("C",end=" ")    
    # print()

#A
#A B
#A B C
#A B C D 
#if n =4
# n=int(input("Enter how many alphabets to print:"))
# for i in range (65,65+n):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

# A B C D E
# A B C D
# A B C
# A B
# A
# n=int(input("Enter how many alphabets to print:"))
# for i in range (65,65+n):
#     for j in range(65,65+n-i+65):
#         print(chr(j),end=" ")
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# n=int(input("Enter how many numbers to print:"))
# for i in range(1,n+1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print() 

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# n=int(input("Enter how many numbers to print:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()    
