import os;
import time;
from multiprocessing import *;
from threading import *;

def fun():
	print("Inside Fun");
	print(os.getpid());
	print(os.getppid());

def gun():
	print("Inside Gun");
	print(os.getpid());
	print(os.getppid());

def run():
	print("Inside Run");
	print(os.getpid());
	print(os.getppid());


def main():

	start=time.time();

	print(os.getpid());
	print(os.getppid());
	fun();

	mp=Process(target=gun,args=())

	mt=Thread(target=run,args=())

	mp.start();
	mt.start();

	mp.join();
	mt.join();



	print(time.time()-start);
	
	time.sleep(10);
	print("After 10 sec");

if(__name__=="__main__"):
	main();
