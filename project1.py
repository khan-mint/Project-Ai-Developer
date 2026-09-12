import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv('students_data2.csv')
print("Data loaded:")
print(df.head()) 
print("\nColumns in CSV:", df.columns.tolist())
X = df[['Study_Hours','Attendance','Past_Marks']] 
y = df['Board_Marks']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"\nAI Accuracy: {accuracy*100:.2f}%")
new_student = [[4, 85, 70]] 
predicted = model.predict(new_student)
print(f"Predicted Board Marks: {predicted[0]:.2f}")