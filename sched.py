from schedule import *;
import time;
import datetime;

def fun_seconds():
	print(datetime.datetime.now());

def main():
	print(datetime.datetime.now());

	every(10).seconds.do(fun_seconds);

	while True:
		run_pending();
		x=1/60;
		x=x+.8;
		print(x);
		time.sleep(1);

if __name__ == '__main__':
	main();

'''def fun():
	print("after 10 sec");

schedule(10,fun());

sleep(9);'''