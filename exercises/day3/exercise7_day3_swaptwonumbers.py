"""
Swapping two integers using bitwise operators.

Input Format:
---------------------------------
Line1, Read an integer
Line2, Read an integer

Output Format:
---------------------------------
Print integers after swapping

Sample Input-1
-----------------------------------
10
20

Sample Output-1
-----------------------------------
20
10

Sample Input-2
-----------------------------------
100
200

Sample Output-2
-----------------------------------
200
100
"""

a = int(input("Enter an integer A: "))
b = int(input("Enter an integer B: "))

a = a ^ b
b = a ^ b
a = a ^ b

print(a)
print(b)