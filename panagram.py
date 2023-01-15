
'''

Solution to Panagram problem on HackerRank
By Mohammed Ahsan Kollathodi 

'''

# input the word.  
word = input()

# Store all the letters in english alphabet as individual strings in a list 
alphabets= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] # To perform lowercase character check
alphabets_caps = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # To perform uppercase character check - at the beginning of the string. 


word = word.lower()
word = word.replace(" ", "")

caplist = []
wordlist = []
updatedlist = []

for i in word :
    if i not in updatedlist:
        updatedlist.append(i)

#print("Updated list:")
#print(updatedlist)

Checkc = all(item in updatedlist for item in alphabets)

if(Checkc == True):
    print("panagram")
else :
    print("not panagram")


capletter = word[0]
caplist.append(capletter)
word = word.replace(capletter,"")
lowerofcpltr = capletter.lower()

for i in word:
    if i not in wordlist:
         wordlist.append(i)

# Extract the starting letter of the string - Capital letter 

# word = word.replace(" ", "")

Refinedlist = []

for i in alphabets:
    if i not in lowerofcpltr:
        Refinedlist.append(i)

#print("Refined list")
#print(Refinedlist)

# We check if all elements of the alphabets list is present in the input wordlist 
# or input wordlist has all elements of the alphabets list. 

#Checka = all(item in wordlist for item in Refinedlist)   # and all(item in alphabets_caps for item in caplist)

#Check to see if the cap letter is present 

#Checkb = any(item in caplist for item in alphabets_caps) 



#Checka = True
#Checkb = False 

#print(Checka)
#print(Checkb)

#print(Check)
# print(Check)


'''
if ((Checka == True) and (Checkb == True)):
    print('pangram')
else :
    print('not pangram')
'''
