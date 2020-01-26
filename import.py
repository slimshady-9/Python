#importing whole file
#import arth;	#all functions

#using from we dont need to import whole file instead we just import single function
#from arth import *;	#import all functions using RegEx 
#import arth;	#imported before using 'from' here

#the arth file is executed after below import call
from arth import add;	#import single function 

print(add(1,5));

if __name__ == '__main__':
	from arth import sub;
	print(sub(8,2));

from arth import mul;
if(1):
	print(mul(2,3));

#div(10,20);	#error as it was not imported