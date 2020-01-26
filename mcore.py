import os;
from multiprocessing import Pool;

def even(no):
	print(os.getpid());
	if(not(no%2)):
		pass;#print(no);

def main():
	print(os.getpid());
	arr=[1,2,3,4,5,6,7,8,9,10];	
	pobj=Pool();
	pobj.map(even,arr);

if(__name__=="__main__"):
	main();