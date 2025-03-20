import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,20,25,30,40]
z=[5,15,25,30,45]

# single Line plot
plt.plot(x,y)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Basic Line Plot")
plt.show()

# Multiple Line Plots in one Graph
plt.plot(x,y,label="Line1",color="blue",marker="s")
plt.plot(x,z,label="Line2",color="red",linestyle="dashed",marker="o")
plt.legend()
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Multi Line Plot")
plt.show()

# formatting plot (style,color,marers)
plt.plot(y,z,linestyle="--",color="orange",marker="d",markersize=8)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Formatting Line Plot")
plt.show()