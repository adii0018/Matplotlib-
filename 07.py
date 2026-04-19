import matplotlib.pyplot as plt

scores =[34,56,19,64,35,67,24,55,87,22,65,66,33,88,99,64]

plt.hist(scores, bins =5, color="purple",edgecolor="black")
plt.xlabel("score range")
plt.ylabel("number of students")
plt.title("score distribution")
plt.show()
