import matplotlib.pyplot as plt
import numpy as np

Students = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Emily'])
SML_Scores = np.array([85, 90, 70, 80, 75])
AD_Scores = np.array([80, 75, 85, 70, 90])
total_Score = np.array(SML_Scores + AD_Scores)

plt.figure(figsize=(13, 9))
plt.subplot(2, 2, 1)
# (A)
plt.bar(Students, SML_Scores)
plt.xlabel("Students")
plt.ylabel("SML Scores")
plt.title("Bar graph showing the SML scores of each student.")
plt.grid()

plt.subplot(2, 2, 2)
# (B)
plt.hist(AD_Scores, bins=4, edgecolor= 'black')
plt.xlabel("AD_Scores")
plt.ylabel("Frequency")
plt.title("Histogram showing the distribution scores")
# plt.grid(True)

plt.subplot(2, 2, 3)
# (C)
plt.scatter(Students, AD_Scores)
plt.scatter(Students, SML_Scores)
for i in range (0, len(Students)):
    plt.annotate("AD", (Students[i], AD_Scores[i]))
    plt.annotate("SML", (Students[i], SML_Scores[i]))
plt.xlabel('Students')
plt.ylabel('Scores')
plt.title('Scatter Plot of SML Scores vs AD Scores')
plt.grid()

plt.subplot(2, 2, 4)
# (D)
plt.pie(total_Score, labels = Students, autopct = '%1.1f%%') # type: ignore
plt.title("Distribution of Scores Across Students (SML & AD)")
plt.legend(Students, loc='best')
plt.axis("equal") 

plt.tight_layout()
# plt.show()
plt.savefig("Student_Performance.png")
