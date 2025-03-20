import matplotlib.pyplot as plt

x=["Apple","Grapes","Oranges","Cherry","Guava","Mango","Berry"]
y=[30,45,15,8,32,12,22]

# Vertical
plt.bar(x,y,color=["r","y","b","g"])
plt.xlabel("Fruits")
plt.ylabel("Sales")
plt.title("Bar Chart (Vertical)")
plt.show()

# Horizontal
plt.barh(x,y,color=["r","y","b","g"])
plt.ylabel("Fruits")
plt.xlabel("Sales")
plt.title("Bar Chart (Horizontal)")
plt.show()