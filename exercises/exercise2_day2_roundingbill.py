"""
Given the Breakfast price 'B', 
tip(gratuity) percent 'T'(the percentage of the 'B' price being added as tip), 
and tax percent 'F'(the percentage of 'B' price being added as tax) 
for a breakfast, 

Find and print the breakfast total cost.
Round the result to the nearest integer.

Note: Use round() in-built function.

Input Format:
------------------------------------------------------
Line 1 : An integer, B, the cost of the meal before tax and tip
Line 2 : An integer, T, the percentage of  being added as tip
Line 3 : An integer, F, the percentage of  being added as tax.

Sample Output:
-------------------------------------------------
Total cost of breakfast.

Sample Input-1
--------------------------------------------
12
20
8

Sample Output-1
--------------------------------------------
15

Explanation:
Total_cost=meal_cost+tip+tax => 12+2.4+0.96=15.36
Tip= meal+tip% => [(12*20)/100]=2.4
Tax=meal+tax% => [ (12*8)/100] = 0.96
"""