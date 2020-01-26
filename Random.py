'''
source=		https://realpython.com/python-random/
random generation is by pseudorandom number generator (PRNG)
seed is number from which a random nuber is generated
this random numbers can be decrypted so it cannot be used for security purposes

for securing this we can use cryptographically secure (csprng)
it uses strings to return entropy of 32 bytes (deemed enough by dev to create noise)

PRNG
it uses mersenne twister=> https://github.com/python/cpython/blob/master/Modules/_randommodule.c

'''

from random import *;

print(random());				#no bet 0 and 1

print(randrange(13,20,3));		#number in 13 to 19 and skip 3 numbers everytime so op=13,16,19

print(uniform(10,20));			#float number betn 10 and 20

lis=[]
for i in range(1,16):
	lis.append(i);

print("List before shuffle\n",*lis,sep=" ")

shuffle(lis);
print("List after shuffling\n",' '.join(map(str,lis)));

print(choice(lis));
print(','.join(map(str,choices(lis,k=4))));
print(choice(range(1,100)));	#no. in 1 to 100

###########################################################################
seed(10);

def notrandom():
	print((10*3)%19);

notrandom();
print(random());	