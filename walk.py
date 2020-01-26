from sys import *;
import os;

def fun(path):

	if(os.path.isabs(path)):
		print("Absolute path");
	else:
		print("Relative path");
		path=os.path.abspath(path);
		print("Absolute path is ",path);

	for Folders,Subfolders,files in os.walk(path):
		print(Folders);
		for f in Subfolders:
			print(f,end="\t");	#prints the sub folders 
		for f in files:
			print(f,end="\t");	#prints the file namess
		print();

def main():
	fun(argv[1]);

if __name__=="__main__":
	main();