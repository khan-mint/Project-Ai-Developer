import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('students.csv')
avg_marks = df.groupby('Subject')['Marks'].mean()
topper = df.loc[df['Marks'].idxmax()]
failed = df[df['Marks'] < 60]
print("Average Marks by Subject:")
print(avg_marks)
print("\nTopper:", topper['Name'], "with", topper['Marks'])
print("\nFailed Students:")
print(failed[['Name','Subject','Marks']])
avg_marks.plot(kind='bar', color=['blue','green'])
plt.title('Average Marks by Subject')
plt.ylabel('Marks')
plt.show()