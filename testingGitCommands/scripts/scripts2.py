#!/usr/bin/env python3
import os
import sys
import math

def check_reboot():
	"""Return Ture if the Computer has a pending reboot """
	return os.path.exist("/run/reboot-required"):
	
def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	print("Every thing is ok in this script")
	sys.exit(0)
def showName(name):
	print("Your name is "+ name)
	
	
main()
print("We import the os module")
print("We import the os module")
print("This is another Print Statement")
print("This is another Print Statement")

print("We import the os module and the line has been added to the print statement")
print("We import the os module")
showName("Farman Khan")


