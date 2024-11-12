import os
import re

def check_first_line(directory, search_string):
	print("\"Part Number\", \"Description\"")
	for filename in os.listdir(directory):
		file_path = os.path.join(directory, filename)
				
		if os.path.isfile(file_path):
			with open(file_path, 'rb') as binary_file:				
				assumed_firstLine = binary_file.read(1000)
				convToAscii = assumed_firstLine.decode('ascii','ignore')
				
				lines = convToAscii.splitlines()
				
				search_bytes = search_string
											
				#search_bytes = search_string.encode('ascii', 'ignore')
				searchName = False
				myfilename = ""

# Formats
# "#- CMNM 013X PCB Assy USB-LED1                                       \"
# "#- CMNM 019X Filter Cable - AC Wires                                 \"
# "#- CMNM 01eCPU Box Cable, 80mm Fan Cables                            \"
# "#- CMNM 01dX, Door Side LEDs Drive Cable                             \"
#				
				for line in lines:
					if searchName:											#if true
						if "CMNM" in line:
							#print(line[8:11])								#get string length
							match = re.search(r'([0-9A-Fa-f]{3})+$', line[8:11])
							if match:
								mynums=match.group()
								myint = int(mynums, 16)
								print("\""+myfilename + ".DRW\", "+"\""+line[11:(11+myint)]+"\"")
							else:
								print( "No number found at the end" )
							break
					elif search_string in line: 							#first line
						searchName = True
						myfilename = filename.split('.')[0]
						#print(myfilename)					
					else:
						break
						
					'''
					if search_string in first_line:
					index = find(search_bytes)
					if index != -1:
						print(f"Found '{search_string}' in {filename}")
						nameIndex = assumed_firstLine.find("CMNM".encode('ascii'))
					

					
					if nameIndex != -1:
						print("found")
						print(assumed_firstLine[nameIndex:nameIndex + 20])
					'''


# Usage
# directory_path = 'path/to/your/directory'

cwd = os.getcwd()
search_string = 'HARNESS_PART'
check_first_line(cwd, search_string)