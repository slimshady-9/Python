num=[1,2,3,4,5];

for x in num:
	print(x);
	#print(num[x]);	# the value in the list is given to x 
	#x+=1;			#automatically iterated
print("break");

i=0;
while(i<len(num)):
	print(num[i]);
	i+=1;
print("break");

for x in range(len(num)):
	#print(x);		#prints index from 0 to length
	print(num[x]);
	x+=1;
print("break");

for j in range(6):
	print(j);
print("break");

for j in range(6,11):
	print(j);
print("break");

for j in range(1,11,3):
	print(j);
print("break");

j=range(1,11,5);
print(j);
for x in j:
	print(x);

