'''
SOLUTION TO CamelCase problem in Python
By Mohammed Ahsan Kollathodi 
Created on 1/13/2023 

'''


# input the string 
# count the number of uppercase letters in the string 
# the total number of words will be number of uppercase letters + 1 



word = input()


count=0
for i in word:
      if(i.isupper()):
            count=count+1
            
# The number of words will be the number of upper characters + 1 with the initial lowecase starting word 

print(count+1)
