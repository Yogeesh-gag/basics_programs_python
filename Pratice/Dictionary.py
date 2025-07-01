# Dictionary

# 1. Write a Python script to sort (ascending and descending) a dictionary by
# value.

'''my_dictinoary={"Yogeesh":23,"Gagan":24,"Rohan":25}
#Ascending 
asc=dict(sorted(my_dictinoary.items(), key=lambda item:item[1]))
dsc=dict(sorted(my_dictinoary.items(), key=lambda item:item[1],reverse=True))
print(f"Ascending order based on value:{asc}")
print(f"Decending order based on value:{dsc}")'''

# 2. Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

'''d = {0: 10, 1: 20}
d[2] = 30

print("Dictionary: ",d)'''

# 3. Write a Python script to concatenate following dictionaries to create a new
# one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
result={}
for i in (dic1,dic2,dic3):
    result.update(i)
print("Concatenated Dictionary: ",result)'''

# 4. Write a Python program to iterate over dictionaries using for loops.

'''my_dictinoary={"Yogeesh":23,"Gagan":24,"Rohan":25}

for key,value in my_dictinoary.items():
    print(key,":",value)'''

# 5. Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

'''n=int(input("Enter a number: "))
squares={X:X*X for X in range(1,n+1)}
print("Squares: ",squares)'''

# 6. Write a Python program to remove a key from a dictionary.

'''my_dictinoary={"Yogeesh":23,"Gagan":24,"Rohan":25}
del my_dictinoary["Yogeesh"]
print(my_dictinoary)'''

# 7. Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

'''Sample_Data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#  Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
unique_values=set()
for dic in Sample_Data:
    for value in dic.values():
        unique_values.add(value)
print("Unique Values: ",unique_values)'''

# 8. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

'''text="Yogi@gag2580"
char_count={}

for char in text:
    char_count[char]=char_count.get(char,0)+1

print(char_count)'''

# 9. Write a Python program to print a dictionary in table format.

'''info={"Name":"Yogeesh","Age":26,"City":"Banglore"}
print("{:<10}{:<10}".format('Key','Value'))
for k,v in info.items():
    print("{:<10}{:<10}".format(k,str(v)))'''

# 10. Write a Python program to count the values associated with key in a
# dictionary.
# Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
# False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
# Expected result: Count of how many dictionaries have success as True

'''data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
 False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

count=sum(x['success']==True for x in data)
print("Count of Success=True: ",count)'''

# 11. Write a Python program to convert a list into a nested dictionary of keys.

'''keys=['a','b','c']
nested=current={}

for k in keys:
    current[k]={}
    current=current[k]

print(nested)'''

# 12. Write a Python program to check multiple keys exists in a dictionary.

''''my_dict={'a':1,'b':2,'c':3}
keys_to_check=['a','b']
if all(k in my_dict for k in keys_to_check):
    print("All Keys are Present...")
else:
    print("Missing keys.")'''

# 13. Write a Python program to count number of items in a dictionary value
# that is a list.
d={'a':[1,2,3],'b':[4,5],'c':10}
count=0

for value in d.values():
    if isinstance(value,list):
        count+=len(value)
print("Total items in list values: ",count)