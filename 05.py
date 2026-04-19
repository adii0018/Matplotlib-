import matplotlib.pyplot as plt

product =["A","b","C","d"]
sales = [200,1500,800,1200]

plt.barh(product,sales, color="red",label="sales of 2026")
plt.xlabel("product")
plt.ylabel("sales")
plt.title("product sales comparison")
plt.legend()
plt.show()