from time import *;

def seperator():
	print("-"*50);

seperator();

x=time();
print(x);
print(type(x));
seperator();


x=ctime();
print(x);
print(type(x));
seperator();

x=gmtime();
print(x);
print(type(x));
seperator();

x=asctime();					#can convert struct_time into string again
print(x);
print(type(x));
seperator();

x=localtime();					#gives struct_time as output
print(x);
print(type(x));

print(x.tm_year);
print(type(x.tm_year));

x=str(x.tm_hour)+str(x.tm_min)+str(x.tm_sec);
print(x);

seperator();