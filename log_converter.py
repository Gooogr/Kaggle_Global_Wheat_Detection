import os
import re
from collections import defaultdict
import json  
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', action = 'store', type = str,
					dest = 'log_file_path', 
					help = 'Path to the log file',
					required = True)

def txt2json(file_path):
	file_lines = open(file_path, 'r').read()
	table_dict = defaultdict()
	current_jpg_name = ''

	jpg_delimiters = " ", "/", ":"
	jpg_regexPattern = '|'.join(map(re.escape, jpg_delimiters))
		
	for line in file_lines.splitlines():	
		if '.jpg' in line:
			for item in re.split(jpg_regexPattern, line):
				if '.jpg' in item:
					current_jpg_name = item
					table_dict[item] = []
		if '%' in line:
			split_string = (re.findall('-?\d+', line))
			split_string = list(filter(lambda x: x != "", split_string)) # remove empty strings from list
			int_string = list(map(int, split_string))
			sub_dict_keys = ['proba_%', 'left_x', 'top_y', 'width', 'height']
			table_dict[current_jpg_name].append(dict(zip(sub_dict_keys, int_string)))	
	return table_dict

if __name__ == "__main__":
	args = parser.parse_args()
	file_path = args.log_file_path
	converted_dict = txt2json(file_path)
	with open("log.json", "w") as outfile:  
		json.dump(converted_dict, outfile)
     


