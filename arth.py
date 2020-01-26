
def add(no1,no2):
	return (no1+no2);

def sub(no1,no2):
	return(no1-no2);

def mul(no1,no2):
	return(no1*no2);

def div(no1,no2):
	if(no2!=0):
		return(no1/no2);
	else:
		return(no2/no1);
def main():
	no1=1;
	no2=2;
	print(add(no1,no2));
	print(sub(no1,no2));
	print(mul(no1,no2));
	print(div(no1,no2));

if(__name__=="__main__"):
	main();

def ifexport():
	if(__name__=="arth"):
		print("arth file has been imported");

ifexport();
