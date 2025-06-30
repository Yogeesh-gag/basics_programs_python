#1. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

'''firsr_name=input("Enter the first name: ")
last_name=input("Enter the second name: ")

print("Reversed order :",last_name,firsr_name)'''

#2 Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

'''data=input("Enter the comma separated numbers:")
items=data.split(",")

print(f"List :{list(items)}")
print(f"Tuple :{tuple(items)}")'''

#3. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

'''color_list = ["Red","Green","White" ,"Black"]
print("First_Color: ",color_list[0])
print("last_color: ",color_list[-1])
print()'''

#4. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result : mat
# abs(number) -> number
# Return the absolute value of the argument.

'''func_name=input("Enter the name of a built-in function name: ")
try:
    func=eval(func_name)
    print(f"\n Documentation for {func_name}:")
    print(func.__doc__)
except NameError:
    print("Invalid function name. Please enter a valid built-in function name")
except Exception as e:
    print("Error:",e)'''

#5. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

'''import calendar

month=int(input("Enter the Month(1-12): "))
year=int(input("Enter the year(eg. 2025): "))
print("Here is the calendar: ")
print(calendar.month(year,month))'''

# 6. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

'''from datetime import date

date1=date(2014,7,2)
date2=date(2014,7,11)

no_of_days=date2-date1
print(f"{no_of_days.days} days")'''

# 7. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False
'''group= [1, 5, 8, 3]
idx=int(input("Enter the to find: "))
if idx in group:
    print("True")
else:
    print("False")'''

# 8. Write a Python program to create a histogram from a given list of integers.

'''list1=[2,3,6,5]
for idx in list1:
    print('*' * idx)'''

# 9. Write a Python program to concatenate all elements in a list into a string and return it.

'''def list_to_string(lst):
    return ''.join(str(x) for x in lst)

print(list_to_string(["Hello"," ","Yogeesh","!"]))'''

# 10. Write a Python program to print out a set containing all the colors from color_list_1 which
# are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# Expected Output :
# {'Black', 'White'}
'''color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1-color_list_2)'''

# 11. Write a Python program to check whether a file exists.

'''import os
file_name='sample.txt'

if os.path.exists(file_name):
    print("File Exists...")
else:
    print("File does not exist...")'''

# 12. Write a python program to call an external command in Python.
# 13. Write a Python program to find out the number of CPUs using.

'''import os
# os.cpu_count() returns the number of available logical CPUs.
print("Number of CPUs: ",os.cpu_count())'''

# 14. Write a Python program to list all files in a directory in Python.

'''import os
directory='.' # current directory
# os.listdir() lists all files and folders in the given directory path.
files=os.listdir(directory)
print("Files and directories: ",files)'''

# 15. Write a python program to access environment variables.

'''import os
# os.environ.get("VAR_NAME") gets the value of an environment variable.
print("Path: ",os.environ.get("PATH"))'''

# 16. Write a Python program to get the current username

'''import getpass
# getpass.getuser() returns the current logged-in user's name.
print("Current username: ",getpass.getuser())'''

# 17. Write a program to get execution time for a Python method.

'''import time
start=time.time()

for i in range(10000):
    if i%2==0:
        print(i,end=" ")

end=time.time()

print("Execution time:",end-start,"seconds")'''

# 18. Write a Python program to get an absolute file path.

'''import os
file_name="sample.txt"
# os.path.abspath() returns the full path of a file relative to current directory.
absolute_path=os.path.abspath("file_name")
print("Absolute path :",absolute_path)'''

# 19. Write a Python program to get file creation and modification date/times.

'''import os
import time

with open("sample.txt","a") as f:
    f.write("Iam adding New Text to the file...")

# with open("sample.txt","r") as f:
#    print(f.read())
# os.path.getctime() → creation time
# os.path.getmtime() → modification time
# time.ctime() → converts timestamps to readable format
print("Created:",time.ctime(os.path.getctime("sample.txt")))
print("Modified:",time.ctime(os.path.getmtime("sample.txt")))'''

# 20. Write a Python program to sort three integers without using conditional statements and
# loops.

'''a,b,c=int(input("Enter the number: ")),int(input("Enter the number: ")),int(input("Enter the number: "))

sorted_list=sorted([a,b,c])
print("Sorted Three Numbers are: ",sorted_list)'''

# 21. Write a Python program to sort files by date.

'''import os

files=os.listdir(".")
files.sort(key=lambda x:os.path.getmtime(x))
# os.path.getmtime() returns the last modified time of a file.
# sort() uses it to arrange files by time.
for file in files:
    print(file,"=>",os.path.getmtime(file))'''

# 22. Write a Python program to get the command-line arguments (name of the script, the number
# of arguments, arguments) passed to a script.

'''import sys

print("Script Name: ",sys.argv[0])
print("Number of arguments: ",len(sys.argv))
print("Arguments: ",sys.argv)'''

# 23. Write a Python program to find the available built-in modules.

'''import sys
print(sys.builtin_module_names)'''

# 24. Write a Python program to get the size of an object in bytes.

'''import sys
x=[2,4,6,9,3]
# sys.getsizeof() returns memory size of an object in bytes.
print("Size of an object in bytes :",sys.getsizeof(x))'''

# 25. Write a Python program to get the current value of the recursion limit.

'''import sys
# Shows how many recursive calls are allowed before Python throws an error.
print("Recursion limit: ",sys.getrecursionlimit())'''

# 26. Write a Python program to count the number occurrence of a specific character in a string.

'''text=input("Enter the sentences: ")
char=input("Enter the character to count: ")
# .count() returns how many times a character appears in a string.
print(f"'{char}' occurs {text.count(char)} times")'''

# 27. Write a Python program to get the system time.

'''import time
# time.ctime() returns the current time as a readable string.
print("Current time in System: ",time.ctime())'''

# 28. Write a Python program to clear the screen or terminal.

'''import os
# cls is for Windows, clear is for macOS/Linux.
os.system('cls' if os.name=='nt' else 'clear')'''

# 29. Write a Python program to get the name of the host on which the routine is running.

'''import socket
# socket.gethostname() returns the name of your machine.
print("Host Name: ",socket.gethostname())'''

# 30. Write a Python program to access and print a URL's content to the console.

'''import urllib.request
respone=urllib.request.urlopen("https://sample.com")
print(respone.read().decode())'''

# 31. Write a Python program to get system command output.

'''import subprocess
# Executes a shell command and captures its output as string.
ouput=subprocess.getoutput("echo Yogesh")
print(ouput)'''

# 32. Write a Python program to get the effective group id, effective user id, real group id, a list of
# supplemental group ids associated with the current process.
# Note: Availability: Unix.

'''import os
print("EUID:", os.geteuid())
print("EGID:", os.getegid())
print("GID:", os.getgid())
print("Groups:", os.getgroups())'''

# 33. Write a Python program to get the users environment.

'''import os
print(dict(os.environ))'''

# 34. Write a Python program to retrieve file properties.

'''import os
import time

file="sample.txt"
print("Size: ",os.path.getsize(file)," bytes")
print("Crated Time: ",time.ctime(os.path.getctime(file)))
print("Modified Time: ",time.ctime(os.path.getmtime(file)))'''

# 35. Write a Python program to get numbers divisible by fifteen from a list using an anonymous
# function.

'''nums=[15,30,45,10,20,25]
div_by_15=list(filter(lambda x: x%15==0,nums))
print("Divisible By 15: ",div_by_15)'''

# 36. Write a Python program to determine if variable is defined or not.

'''try:
    print(x)
except NameError:
    print("Vaiable x is not defined")'''

# 37. Write a Python program to empty a variable without destroying it.
# Sample data: n=20
# d = {"x":200}
# Expected Output : 0
# {}

'''n=10
d={"x":200}
n=0
d.clear()
print(n)
print(d)'''

# 38. Write a Python program to add leading zeroes to a string.

'''s="42"
# .zfill(width) pads the string with zeros to the left.
print(s.zfill(5))'''

# 39. Write a Python program to find files and skip directories of a given directory.

'''import os
# os.path.isfile() ensures only files are printed.
for item in os.listdir('.'):
    if os.path.isfile(item):
        print(item)'''

# 40. Write a Python program to extract single key-value pair of a dictionary in variables.

'''d={
    "x":100
}
key,value=list(d.items())[0]
print("Key: ",key)
print("Value: ",value)'''

# 41. Write a Python program to convert an integer to binary keep leading zeros.
# Sample data : 50
# Expected output : 00001100, 0000001100

'''data=12
print(format(data,'08b'))
print(format(data,'010b'))'''

# 42. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode
# on operating system.

'''import struct

print("Python runs in",struct.calcsize("P")*8,"bit mode")'''

# 43. Write a Python function to find the maximum and minimum numbers from a sequence of
# numbers.
# Note: Do not use built-in functions.

def find_min_max(lst):
    min=max=lst[0]
    for num in lst[1:]:
        if num<min:
            min=num
        if num>max:
            max=num
    return min,max

numbers=[4,10,2,8,14,20]
min,max=find_min_max(numbers)
print("Maximum Number is:",max)
print("Minimum Number is: ",min)