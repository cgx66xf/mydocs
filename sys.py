"""
import sys

sys.stderr.write('This is stderr text\n')  #prints out an error msg
sys.stderr.flush()
sys.stdout.write('This is stdout text\n') #prints out a blue msg 

print(sys.argv) #when we run sys.py in command line this line outputs the arguments for ex:  bash>sys.py hello motherfucker  output: ['sys.py', 'hello', 'motherfucker']

if (len(sys.argv) > 1):
	print(sys.argv[1])
	
	
def main(sys.argv[1]):
	print(sys.argv[1])
"""

#-------------------------------argparse--------------------------
"""
import argparse 
#Interfaces with the python system module to grab the arguments from the command line

def times5(n):
	n= n*5
	return n

def main():
	parser= argparse.ArgumentParser()
	parser.add_argument("num", help= "The number that you want to add 5 to", type= int)
	args= parser.parse_args()
	print(str(args.num),"times 5 is:",str(times5(args.num)))

if __name__ == '__main__' :
	main()
"""		
#conditional arguments
#parser.add_argument("--stealth", help= "scans in stealth", action= "store_true")	

