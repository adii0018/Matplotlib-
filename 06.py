import matplotlib.pyplot as plt 

teams =["Rcb❤️","Mi❄️","Csk🌿","lsg☁️"]
score =[100,80,40,22]

plt.pie(score,labels=teams,autopct="%1.1f%%",colors=["red","blue","yellow","pink"])
plt.title("ipl teams ❤️")
plt.legend(loc="lower left")
plt.show()