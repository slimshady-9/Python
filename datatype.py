no = 0;

print(no);
print(id(no))
print(type(no));

no="String";

print(no);
print(id(no))
print(type(no));

no=8.8888888888;

print(no);
print(id(no))
print(type(no));

no=(1,2,3,4);

print(no);
print(id(no))
print(type(no));

no={1,2,3,4};

print(no);
print(id(no))
print(type(no));

no=[1,2,3,4];

print(no);
print(id(no))
print(type(no));

x=(1,2,3,4);
print(x);
print(id(x));  #same id
x=(1,2,3);
print(x);
print(id(x));  #different id

x={1,2,3,4};   
print(x);
print(id(x));  #same id
x={1,2,3};	 #once 1 set having exact same value are assigned they arent repeated for other subsets 
print(x);
print(id(x));	#same id

x=[1,2,3,4];
print(x);
print(id(x));  #different id
x=[1,2,3];
print(x);
print(id(x));	#different id
