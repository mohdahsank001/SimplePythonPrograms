'''
Solution by Mohammed Ahsan Kollathodi 
To the HackerRank problem Gemstones 

'''
# Collection of rocks with each rock having various minerals in it, a word with different letters would represent a rock.
# Each type of mineral is represented through a lower case letter in the range a-z
# There many be multiple occrences of minerals in a rock, ie there may be multiple occurances of the same letter in different words. 
# A mineral is called a gemstone if it occurs atleast once in each of these rocks, or a letter appearing atleast once in each of these words. 

# input n - the size of the array 
n = input()
n = int(n)
# initialize the mineral count as 0
count = 0 


# input the strings into the array , corresponding to the rock where each letter in a word represents a mineral and a word represents a rock 

rocks = []  # Initialise a list to store the rock names
while True:
    try:
        line = input()
    except EOFError:
        break
    rocks.append((line)) # add the rock names to the list
#TEST

#print(rocks)
# find intersection among the list of all elements in the list by considering it as a map and  

common = set.intersection(*map(set,rocks))

# print the number of common elements in the strings to get common occurance

print(len(common))
