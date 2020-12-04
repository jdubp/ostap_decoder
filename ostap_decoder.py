import re

# File to examine (change based on file name)
file = 'input_file.txt'

# Regex patterns (change based on file)
array_0 = re.compile(r'[a-z0-9]+\[0\].\=.[0-9]+;$',re.I) # jhfroad7[0] = 1;
array_1 = re.compile(r'[a-z0-9]+\[1\].\=.[0-9]+;$', re.I) #jhfroad7[1] = 101; 

# List to hold integers
int_list = []

# List to hold combined integers
to_char_code_list = []

# Final output list
output = []

# Get return functions and keys lists
with open(file, 'r') as f:
	for line in f:
		array_0_match = re.search(array_0, line)
		array_1_match = re.search(array_1, line)
		if array_0_match: 
			array_0_line = array_0_match.group()
			array_0_split = array_0_line.split(' ')
			array_0_num = array_0_split[-1].replace(';','')
			int_list.append(array_0_num)
		if array_1_match:	
			array_1_line = array_1_match.group()
			array_1_split = array_1_line.split(' ')
			array_1_num = array_1_split[-1].replace(';','')
			int_list.append(array_1_num)
print(int_list)
# Split int_list into lists of 2
l = [ int_list [i:i + 2] for i in range(0,len(int_list),2) ]
# Add each grouping of two ints together
# The below code may need changed if addition is not being used
counter = 0
while counter != len(l):
	for each in l:
		num = int(each[0]) + int(each[1])
		to_char_code_list.append(num)
		counter = counter+1

# Print final output from ints	
for each in to_char_code_list:
	try:
		output.append(chr(each))
	except:
		pass

# Join final output
print(''.join(output).encode('utf-8'))