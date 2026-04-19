import matplotlib.pyplot as plt 

plt.scatter([1,2,3],[50,55,60],color="blue",label="class A",marker="^") # group A
plt.scatter([1,2,3],[40,75,80],color="green",label="class B") # group B
plt.xlabel("hours study")
plt.ylabel("exam score")
plt.title("realtion btw two class")
plt.legend()
plt.grid(True)
plt.show()
