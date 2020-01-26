import pandas as pd;

sep="_"*55;
data=[1,2,3,4,5];
datax=[[1,'Ketan'],[2,'sLiM'],[3,'ShAdY']];

dataxx={'x':pd.Series(data,index=['a','b','c','d','e']),'y':pd.Series(index=[11,22,33])}
#dataxx=[pd.Series(data,index=['a','b','c','d','e']),pd.Series(datax,index=[11,22,33])]		if you want it horizonal instead of vertical

print(sep);print(sep);
#####DATASERIES#####

ds=pd.Series();
print(ds);
print(type(ds))

print(sep);

ds=pd.Series(data);
print(ds);

print(sep);

ds=pd.Series(datax);
print(ds);

print(sep);

ds=pd.Series(datax,index=[10,20,30]);
print(ds); 

ds=pd.Series(dataxx);
print(ds);

print(sep);print(sep);

#######DATAFRAME######

df=pd.DataFrame();
print(df);
print(type(df))

print(sep);

df=pd.DataFrame(datax);
print(df);

print(sep);

df=pd.DataFrame(datax);
print(df);

print(sep);

df=pd.DataFrame(datax,columns=['first','second']);
print(df);

print(sep);

df=pd.DataFrame(dataxx);
print(df);

print(sep);print(sep);

print("Writing a csv using PANDAS\n\n");

df1=pd.DataFrame(datax,columns=['first','second']);

df1.to_excel('pdwrtcsv.xlsx',sheet_name="S1");

df2=pd.DataFrame(dataxx);

writer=pd.ExcelWriter('pdwrtcsv1.xlsx',engine='xlsxwriter');
df2.to_excel(writer,sheet_name='Sheet1');
writer.save();

print("Succesfully written File");

print(sep);print(sep);

######Importin file from outside and using it by pandas##########
print("Accessing a csv file");

excel_file="C:\Programming\Python\Python\ML\Marvellous.xlsx";
file_data= pd.read_excel(excel_file);

print("Printing Heads i.e. first 5\n",file_data.head());

file_sheet1=pd.read_excel(excel_file,sheet_name=0,index_col=0);		#sheet_name-which sheet in the file,index_col-makes that column the index
print("\nName as its index\n",file_sheet1.head())		#prints name as its index

xlsx=pd.ExcelFile(excel_file);
file_sheets=[];

for sheet in xlsx.sheet_names:
	print(sheet);
	file_sheets.append(xlsx.parse(sheet));


file_data=pd.concat(file_sheets)
print(file_data)
