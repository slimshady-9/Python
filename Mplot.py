import pandas as pd
import matplotlib.pyplot as plt

excel_file='C:\Programming\Python\Python\ML\Marvellous.xlsx';
data=pd.read_excel(excel_file);

data['Age'].plot(kind="hist")
plt.show();

data['Age'].plot(kind="barh")
plt.show();

sorted_data=data.sort_values(["Name"]);
print(sorted_data.head(3));

sorted_data['Age'].plot(kind="barh");
plt.show();