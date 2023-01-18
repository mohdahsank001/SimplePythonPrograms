'''
Solution by Mohammed Ahsan Kollathodi
Python program to find the median of a list of numbers. 

'''


import re as re 




n1 = input()
# Input the string of numbers 
arr1 = input()


# Extract numbers as int from the string of numbers.  
def extractor(string):
    return [int(s) for s in re.findall(r"-?\d+", string)]   
list1 = extractor(arr1)


# list of elements to calculate median
n_num = list1
n = len(n_num)
n_num.sort()

if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
    
# Output the median 
print(str(median))


