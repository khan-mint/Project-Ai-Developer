import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV
df = pd.read_csv('students.csv')

# Set style so graphs look nice
plt.style.use('ggplot')

# ===== CHART 1: BAR CHART - Average Marks per Subject =====
avg_marks = df.groupby('Subject')['Marks'].mean()

plt.figure(figsize=(6,4))  # size of graph
avg_marks.plot(kind='bar', color=['skyblue','lightgreen'])
plt.title('Average Marks by Subject')
plt.ylabel('Average Marks')
plt.xlabel('Subject')
plt.xticks(rotation=0)  # keep subject names straight
plt.show()

# ===== CHART 2: HISTOGRAM - Distribution of All Marks =====
plt.figure(figsize=(6,4))
plt.hist(df['Marks'], bins=5, color='orange', edgecolor='black')
plt.title('Distribution of Student Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()

# ===== CHART 3: PIE CHART - Grade Distribution =====
grade_counts = df['Grade'].value_counts()

plt.figure(figsize=(5,5))
plt.pie(grade_counts, labels=grade_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Grade Distribution')
plt.show()