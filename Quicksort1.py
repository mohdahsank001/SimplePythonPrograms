 
import re

'''
Solution to the QuickSort1 Challenge on Hackerrank 

Solution by Mohammed Ahsan Kollathodi. 

'''



# input the size of the array. 
n = input()



'''
input n spaced integers arr[i] (the unsorted array), the first integer being arr[0] and the pivot element being p
arr[0] is the pivot element 
n = input()
input n spaced integers arr[i] (the unsorted array), the first integer being arr[0] and the pivot element being p
arr[0] is the pivot element 
'''


# Import the input array. 
arr1 = input()


# Extract numbers as int from the string of numbers.  
def extractor(string):
    return [int(s) for s in re.findall(r"-?\d+", string)]   

# Extracted list consists of all the numbers from the string. 
list1 = extractor(arr1)



# perform the partition
def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high] 
   for j in range(low , high):
      if arr[j] <= pivot:
         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

   
# Do the quick sort 
def quickSort(arr,low,high):
   if low < high:
      pi = partition(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)

      
#Produce the output
arr = list1
n = len(arr)
quickSort(arr,0,n-1)
for i in range(n):
   print (arr[i],end=" ")

