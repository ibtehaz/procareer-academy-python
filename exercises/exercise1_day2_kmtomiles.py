"""John is travelling from Austin to Dallas by road. 
He sees the Google map to get an idea of time taken to reach Dallas and the distance. 
Google map shows the distance in Kilometers. 

Help John to convert the distance from Kilometers to miles.

Note: 
1 Kilometer= 0.621 Miles

Input Format:
------------------------------------
Enter the distance - Float value

Output Format:
-------------------------------------
Floating point value - Kilometers converted to Miles


Sample Input-1
------------------------------------
45.2

Sample Output-1
------------------------------------
28.0692


Sample Input-2
------------------------------------
12

Sample Output-2
---------------------------------------
7.452
"""

distance_in_km = float(input("Enter the distance: "))
distance_in_miles = distance_in_km * 0.621
print(distance_in_miles)
