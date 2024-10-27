'''
Question as Follows:
In the bustling markets of Delhi, Neha is fascinated by numbers that are strong, where the sum of the factorial of its digits equals the number itself. Help Neha by writing a python program that identifies and prints all strong numbers within a given range a to b(both inclusive).

Definition of Strong Number: A number is called a strong number if the sum of the factorial of its digits equals the number itself. For example, 145 is a strong number because 1! + 4! + 5! = 1 + 24 + 120 = 145.
Factorial- In mathematics, the factorial of a non-negative integer, is the product of all positive integers less than or equal to.

Note:-
This is a functional problem. You do not need to take any input. You just need to complete the function, and print the output.
Input
First Line will contain an integer a representing the start of the range.
Second Line will contain an integer b representing the end of the range.

Constraint:
1<= a <=10000
1 <= b <= 10000
Output
Print all strong numbers between a and b.
'''
#Answers as Follows:
def find_strong_numbers_in_range(a, b):
    for i in range(a,b+1):
        n=i
        s=0
        while n>0:
            a=n%10
            n//=10
            p=1
            for j in range(1,a+1):
                 p*=j
            s+=p
        if i==s:
            print(i)
