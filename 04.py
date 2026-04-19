import matplotlib.pyplot as plt
x =[1,2,3,4]
# horizontal axis
y =[20,35,14,88]
# vertical axis
plt.grid()
plt.xticks([1,2,3,4],["m1","m2","m3","m4"])
plt.plot(x,y)
plt.savefig("line plot.png",dpi=400,bbox_inches="tight")

plt.show()