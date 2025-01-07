Q1. Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n


def sum_of_even_integers(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i
    return sum

n=int(input("Enter a positive integer to calculate even number till the number "))   
result=sum_of_even_integers(n)
print(f"Sum of even number till {n} values is ",result)
