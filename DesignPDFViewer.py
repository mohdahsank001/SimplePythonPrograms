

'''
Solution by Mohammed Ahsan Kollathodi 
Created on 1/10/2023
Solution to the Design PDF Viewer on HackerRank

'''

# the value of height corresponds to the value at index of the letter in 26 character set starting from a equal to 0 and z equal to 25 in the given array - height array given
# All letters are assumed to 1 mm wide 
# width will be cumulative sum of all the letters present in the word, if there are 4 letters the width will be 4. 
# The height is considered to be the highest value among the given array values for a particular index position 




# input number string into a list and split into individual numbers
n = input().split()
# input word string
w = input().split()

# introduce list to store the inidividual numbers - corresponding to the height
list1 = []

# for each element in the input string, convert the string literal to int
for x in n : 
    x = int(x)
    list1.append(x)   # add the inidividual integer to the list 


# add individual letters of the string to a list 
# print(type(w[0]))
# The string is at index 0 of the list
t = w[0]

# Create a new list to store the individual letters 
lista = []

# Add individual letters in the string into a list
for letter in t:
    lista.append(letter)
    
# list to store heights
listht = []

for i in  lista:
# print the first letter of list a to get the height corresponding letter 
    if i == 'a' : 
        height = list1[0]
    elif i == 'b':
        height = list1[1]
    elif i == 'c':
        height = list1[2]
    elif i == 'd':
        height = list1[3]
    elif i == 'e':
        height = list1[4]
    elif i == 'f':
        height = list1[5]
    elif i == 'g':
        height = list1[6]
    elif i == 'h':
        height = list1[7]
    elif i == 'i':
        height = list1[8]
    elif i == 'j':
        height = list1[9]
    elif i == 'k':
        height = list1[10]
    elif i == 'l':
        height = list1[11]
    elif i == 'm':
        height = list1[12]
    elif i == 'n':
        height = list1[13]
    elif i == 'o':
        height = list1[14]
    elif i == 'p':
        height = list1[15]
    elif i == 'q':
        height = list1[16]
    elif i == 'r':
        height = list1[17]
    elif i == 's':
        height = list1[18]
    elif i == 't':
        height = list1[19]
    elif i == 'u':
        height = list1[20]
    elif i == 'v':
        height = list1[21]
    elif i == 'w':
        height = list1[22]
    elif i == 'x':
        height = list1[23]
    elif i == 'y':
        height = list1[24]
    elif i == 'z':
        height = list1[25]
    listht.append(height)
    
# compute width 
width = len(t)


# compute tallest height from the given array
fheight = max(listht)



# Compute the area 

area = width * fheight

print(area)
# test 
