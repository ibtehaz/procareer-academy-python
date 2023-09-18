"""
John has just started Programming, he is in first year of Engineering.
John is reading about Relational Operators.
Relational Operators are operators which check the relationship between two 
values.

 Ask John to read integers A and B. Your task is to help John find the 
 relationship between A and B.
 
Input Format:
-----------------------------------------------
Read two Integers A and B


Output Format:
-----------------------------------------------
Print operator <,>,= which meets the condition


Sample Input-1
----------------------------
10
20

Sample Output-1
-----------------------------
<

Sample Input-2
------------------------------
20
20

Sample Output-2
------------------------------
=
"""

a = int(input("Enter integer A: "))
b = int(input("Enter integer B: "))

op = ""

if a > b:
    op = ">"
elif a < b:
    op = "<"
else:
    op = "="

print(op)