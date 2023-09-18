"""
Write a python program to read two numbers 'N1' and 'N2', find out the maximum of 'N1' and 'N2'.

Input Format:
---------------------------------
Line 1 : An integer, N1
Line 2 : An integer, N2

Output Format:
---------------------------------
An integer, Print maximum number of N1 and N2


Sample Input-1:
---------------------------------
1
2

Sample Output-1:
---------------------------------
2

Sample Input-2
---------------------------------
-1
0

Sample Output-2
---------------------------------
0
"""

n1 = int(input("Enter an integer, N1: "))
n2 = int(input("Enter an integer, N2: "))

max = n1 if n1 > n2 else n2

print(max)