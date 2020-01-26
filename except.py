	
def main():
	try:
		x=5/0;
	except ZeroDivisionError:
		print("Exception occured");
	finally:
		print("in finally");

if __name__=="__main__":
	main();