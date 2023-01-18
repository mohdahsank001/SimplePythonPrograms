'''
SOLUTION TO Super Reduced String IN Python (HACKERRANK) 
By Mohammed Ahsan Kollathodi
'''




# Input the string. 
input_string = input()



# Function to remove duplicate adjacent characters in an input string. 

def ShortenString(str1):
	
	# Store the string without duplicate elements
	st = []
	
	# Store the index of the string
	i = 0
	
	# Traverse the string string
	while i < len(str1):
		
		# Checks if stack is empty or top of the and stack is not equal to current character
		if len(st)== 0 or str1[i] != st[-1]:
			st.append(str1[i])
			i += 1
			
		# If top element of the stack is equal to the current character
		else:
			st.pop()
			i += 1
			
	# If stack is returning empty
	if len(st)== 0:
		return("Empty String")
		
	# If stack is not returning Empty
	else:
		short_string = ""
		for i in st:
			short_string += str(i)
		return(short_string)
















    






