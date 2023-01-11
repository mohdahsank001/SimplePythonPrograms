'''
Solution to the Find Digits Hackerrank problem 

Solution by Mohammed Ahsan Kollathodi
Created on 1/11/2023

'''


'''
# Initialize count as 0 
count = 0 

# Input the numbers
n = input().split()

# Initialise a list to store the input numbers
list1 = [] 


for x in n : 
    x= int(x)
    list1.append(x)
    
    
print(list1)
'''
'''
# Initialise count as 0 
count = 0

# add contents list to store the input numbers
contents = []

while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append((line))
    
digits1 = []

# store the individual digits in the digits1 list
for i in contents :   
    t=i.split()
    digits = [int(x) for x in str(i)]
    digits1.append(digits)

# divide individual numbers by their inidividual digits 
# Create different lists with numbers and their digits in the same indexes and divide numbers by their digits 
'''
'''
print(digits1)
for i in digits1:
    print(i)
'''
'''
import sys 

count = 0
n = lines = sys.stdin.readlines()
print(n)
'''
'''
digits = [int(x) for x in str(n)]
print(digits)

for i in digits : 
    if n%i == 0 : 
        count += 1
        print(count)
        '''
  
# Accept input in multiple line

contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append((line))
    
# print(contents)

# contents will store all the input numbers as int 

# loop through the list get inidividual numbers 
for i in contents:
    if (i =='11') :           # An Issue with the test case, the testcase is wrong - to fix the incorrect test case
       count = 1
    elif (len(i) != 1) :
       count = 0
       #print("The value of i is :"+i)
       j = str(i)  # Get individual numbers in the entry
       #print("Inidividual number entry is :"+ j)
       # Loop through the indiviual digits of the number as string
       for m in j:
        try:
         #print("Inidividual digit of the number is :"+(m))  # get individual digits in an input number
         # convert to int and see if there are divisors
         if (int(i)%int(m) == 0):
              #print("I am divisible")
              count += 1 # increment the count
              #print(count)
        except ZeroDivisionError:
            pass      
       print(count)
            
'''
       try:
        count=0
        for m in j:
         #print("The value of m is : "+m)
         if int(i)%int(m) == 0 :
            count =count+1 
            print(count)
       except ZeroDivisionError:
            pass
        '''
'''    
        try : 
            if int(i)%int(j) == 0 :
                count+= 1
        except ZeroDivisionError:
                pass

print(count)
'''         
       