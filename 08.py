import matplotlib.pyplot as plt 
hours_study =[1,2,3,4,5]
exam_score =[50,60,70,77,90]
plt.scatter(hours_study,exam_score,color="green",marker="o",label="student data ")
plt.xlabel("hours study")
plt.ylabel("exam score")
plt.title("realtion btw study and marks")
plt.legend()
plt.grid(True)
plt.show()
