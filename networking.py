import re

'''
fhandle = open('mbox.txt')
for line in fhandle:
	striped_line = line.rstrip()
	matches = re.findall('^X\S*:([0-9.]+)', striped_line)
	if len(matches) > 0:
		print(matches)	
'''

hand = open('mbox.txt')
for line in hand:
	line = line.rstrip()
	x = re.findall('\S+@\S+', line)
	if len(x) > 0:
		print (x)

