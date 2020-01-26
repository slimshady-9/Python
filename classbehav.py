class Demo:
	no=0;
	def fun(self):
		print("Inside instance behaviour");

	@classmethod
	def gun(cls):
		print("inside class behaviour");
		print(cls.no);

	def gunx():
		print("Another static behaviour");
		print(Demo.no);

	@staticmethod
	def run():
		print("inside static method");
		print(Demo.no);	

obj=Demo();
obj.fun();
Demo.gun();
Demo.gunx();
Demo.run();