import random
from subprocess import call
#Please edit the path before you run the script
file = open("/path/to/wordlist")
num_lines = 2619
line_no = random.randrange(0,num_lines,2)
for i, line in enumerate(file):
	if i == line_no:
		word = line
		definition = file.next()
		break
file.close()
call(["notify-send",word,definition])