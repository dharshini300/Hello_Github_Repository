import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied":[2,5,6,7,3,5,4,8,6,9],
    "Attendance":[80,70,90,70,56,90,80,95,85,98],
    "Previous_Score":[45,78,90,67,90,97,87,88,76,95],
    "Final_Score":[67,89,98,68,89,98,67,95,85,99],
    "Sleep_Hours":[6,7,8,5,6,8,7,9,6,8],
    "Assignments":[5,8,9,6,7,10,8,9,7,10],
    "Study_Material":[1,2,3,2,1,3,2,3,2,3],
    "Test_Attempts":[2,3,4,2,3,5,3,4,2,5],
    "Class_Participation":[70,80,90,60,75,95,85,90,70,98],
    "Revision_Hours":[1,2,3,1,2,4,2,3,2,5]
}

df = pd.DataFrame(data)

print(df.head())
print("Shape:",df.shape)
print(df.isnull().sum())

sns.barplot(data=df,x="Hours_Studied",y="Final_Score")
plt.title("Study Hour vs Final Score")
plt.show()
