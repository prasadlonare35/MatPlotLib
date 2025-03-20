import matplotlib.pyplot as plt

x=["Apple","Grapes","Oranges","Cherry","Guava","Mango","Berry"]
y=[30,45,15,8,32,12,22]

plt.pie(y,labels=x,autopct="%1.1f%%",colors=["r","y","b","g"])
plt.show()