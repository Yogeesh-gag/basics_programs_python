# 1. Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.

'''import array
#Create an array of 5 integers 
arr=array.array('i',[10,20,30,40,50])
#Display the array items
print("Array elements:",arr.tolist())

# Access elements by index
print("First element:", arr[0])
print("Third element:", arr[2])
print("Last element:", arr[-1])'''

# 2. Write a Python program to reverse the order of the items in the array.

import array
arr = array.array('i', [10, 20, 30, 40, 50])
# Reverse the array
arr.reverse()
print("Reversed array:", arr.tolist())

# 3. Write a Python program to get the number of occurrences of a specified element in an
# array.
# 4. Write a Python program to remove the first occurrence of a specified element from an
# array.