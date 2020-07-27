import os
import re

FILE_PATH = './log_naive.txt'

file_lines = open(FILE_PATH, 'r').read()

# Get jpg files names
delimiters = " ", "/", ":"
regexPattern = '|'.join(map(re.escape, delimiters))

jpg_names = []
	
for item in re.split(regexPattern, file_lines):
	if '.jpg' in item:
		jpg_names.append(item)
		
print(jpg_names)
		



