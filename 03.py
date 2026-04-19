import matplotlib.pyplot as plt

months =[1,2,3,4]
sales =[300,400,500,800]

plt.plot(months, sales, color="green", linestyle='--',linewidth="1",marker="o",label="data of sales")

plt.xlabel("months")
plt.ylabel("sales per month")
plt.title("sales chart")
plt.grid(color="gray",linestyle=":")
plt.legend()
plt.show()
