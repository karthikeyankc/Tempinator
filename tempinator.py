import os
import shutil
print """
Tempinator v0.1 by Karthikeyan KC
A simple program written in Python that cleans the Temp directory in a Windows machine.
"""
temp_path = os.path.expanduser('~')+'\AppData\Local\\Temp'
file_list = os.listdir(temp_path)
for file in file_list:
	file_path = os.path.join(temp_path, file)
	if os.path.isdir(file_path):
		shutil.rmtree(file_path, ignore_errors=True, onerror=None)
	else:
		try:
			os.remove(file_path)
		except WindowsError:
			continue
try:
	if os.listdir(temp_path) == []:
		print "Tempinator just terminated all files!"
	else:
		print "Some of these files couldn't be removed.\nTry closing any active applications and running it again.\n"
		for file in os.listdir(temp_path):
			print "%s" %file
except:
	"Directory not found!"
raw_input("\nPress any key to exit!")