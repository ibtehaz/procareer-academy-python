"""
Read three numbers from the user, find the maximum of three.

Input Format:
--------------------------------
Read 3 integers

Output Format:
----------------------------------
Print maximum integer


Sample Input-1
----------------------------------
1
2
3

Sample Output-1
------------------------------------
3

Sample Input-2
------------------------------------
-22
0
-43

Sample Output-2
-------------------------------------
0
"""
a = int(input())
b = int(input())
c = int(input())

max = 0

if  a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

print(max)