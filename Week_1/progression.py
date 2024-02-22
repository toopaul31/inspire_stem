# this is a program used to calculate terms on a sequence
# date : 21/02/2024
# name : paul too
import math

#arithmetic sequence

a = int(input("the first term of the sequence :"))
n = int(input("the number of sequnce :"))
d = int(input("the common diff :"))

an = a + (n-1)*d

print("the term in the arithmetic :",an)

# geometric sequence

a = int(input("the first term of the sequence :"))
n = int(input("the number of sequence :"))
r = int(input("the common ratio :"))

ar = a*r**(n-1)

print("the term in the geometric :",ar)